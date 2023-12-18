# coding=utf-8
from typing import *

from node import *



class Function:
    """
    表示一个函数的类。

    此类用于封装函数的定义，包括函数名、参数名列表和函数体。

    Attributes:
        name (str): 函数的名称。
        arg_names (List[str]): 函数的参数名列表。
        body (_node): 函数的主体，是一个节点对象。
    """

    def __init__(self, name: str, arg_names: List[str], body: '_node'):
        """
        初始化函数对象。

        Args:
            name (str): 函数的名称。
            arg_names (List[str]): 函数的参数名列表。
            body (_node): 函数的主体，是一个节点对象。
        """
        self.name: str = name
        self.arg_names: List[str] = arg_names
        self.body: '_node' = body

    def __repr__(self) -> str:
        """
        返回函数对象的字符串表示形式
        Returns:
            str: 描述函数对象的字符串，包括其名称。
        """
        return f"<Function object '{self.name}'>"

    def exec(self, env: Optional['Translator'], args: List[Any]) -> Tuple[Any, 'Translator']:
        """
        执行函数。

        根据提供的环境和参数列表执行函数。创建一个新的翻译器实例来执行函数体。

        Args:
            env (Optional[Translator]): 函数执行的环境。
            args (List[Any]): 函数执行时的参数列表。

        Returns:
            Tuple[Any, Translator]: 函数的返回值和执行后的翻译器实例。
        """
        etb: Dict[str, Any] = {self.name: self}
        for k, v in zip(self.arg_names, args):
            etb[k] = v
        if env is None:
            tran = Translator(self.body, extend_table=etb)
        else:
            tran = Translator(self.body, tb=env.var_table, extend_table=etb)
        ret = tran.translate()
        return ret, tran


class Class:
    """
    表示一个Python类的对象。

    此类负责解析并存储类定义中的函数。它使用 'Translator' 来翻译类中的函数，
    并将翻译后的函数存储在自身的 'functions' 属性中。

    Attributes:
        name (str): 类的名称。
        functions (dict): 一个包含类中函数的字典，其中键是函数名称，值是函数的表示。
    """

    def __init__(self, name: str, funcs: List[Any]) -> None:
        """
        初始化Class对象。

        使用提供的类名和函数列表初始化Class对象。它创建一个 'Translator' 实例，
        并用它来翻译类中的函数。

        Args:
            name (str): 类的名称。
            funcs (List[Any]): 类中函数的列表。每个函数应该是一个可被 'Translator' 翻译的对象。
        """
        self.name: str = name
        tran = Translator(funcs)
        tran.translate()
        self.functions: Dict[str, Any] = tran.var_table

    def __repr__(self) -> str:
        """
        返回Class对象的字符串表示。

        当打印或查看Class对象时，此方法提供了一个便于阅读的表示形式。

        Returns:
            str: 描述Class对象的字符串，包括其名称。
        """
        return f"<Class object '{self.name}'>"


class PyObject:
    """
    代表一个Python对象。

    此类用于模拟Python中的对象，包括类属性和构造函数的执行。

    Attributes:
        cls (Any): 该对象所属的类。
        props (Dict[str, Any]): 存储对象属性的字典。
    """

    def __init__(self, cls: Any) -> None:
        """初始化PyObject对象。

        Args:
            cls (Any): 对象所属的类。
        """
        self.cls: Any = cls
        self.props: Dict[str, Any] = {}
        self.props.update(self.cls.functions)

    def __repr__(self) -> str:
        """返回对象的字符串表示。

        Returns:
            str: 对象的字符串表示。
        """
        address = hex(id(self))
        return f"<PyObject {self.cls.name} at {address}>"

    def constructor(self, args: List[Any]) -> None:
        """执行类的构造函数。

        如果定义了 '__init__' 方法，则调用它。否则，使用默认构造函数。

        Args:
            args (List[Any]): 传递给构造函数的参数列表。

        Raises:
            AssertionError: 如果没有 '__init__' 方法且传递了参数。
            AttributeError: 如果试图访问不存在的属性。
        """
        if self.cls.functions.get('__init__', None) is None:
            assert len(args) == 0, "default constructor doesn't need argument(s)!"
            return
        _, tran = self.cls.functions['__init__'].exec(env=None, args=[self] + args)
        for name, value in tran.var_table.items():
            self.props[name] = value

    def __getitem__(self, item: str) -> Any:
        """获取对象的属性值。

        Args:
            item (str): 属性名。

        Returns:
            Any: 属性值。

        Raises:
            AssertionError: 如果 'item' 不是字符串。
            AttributeError: 如果属性不存在。
        """
        assert isinstance(item, str)
        if self.props.get(item, None) is None:
            raise AttributeError(f"'{self.cls.name}' object has no attribute '{item}'")
        return self.props[item]

    def __setitem__(self, key: str, value: Any) -> None:
        """设置对象的属性值。

        Args:
            key (str): 属性名。
            value (Any): 要设置的值。

        Raises:
            AssertionError: 如果 'key' 不是字符串。
        """
        assert isinstance(key, str)
        self.props[key] = value


class Translator:
    @staticmethod
    def get_value(tb, vid):
        name, sub = vid
        if not isinstance(name, tuple):
            if sub is None:
                return tb[name]
            return tb[name][sub]
        if sub is None:
            return Translator.get_value(tb, name)
        return Translator.get_value(tb, name)[sub]

    @staticmethod
    def set_value(tb, vid, val):
        name, sub = vid
        if not isinstance(name, tuple):
            if sub is None:
                tb[name] = val
                return
            tb[name][sub] = val
            return
        if sub is None:
            Translator.set_value(tb, name, val)
            return
        Translator.get_value(tb, name)[sub] = val

    def __init__(self, tree, tb=None, loop=0, break_flag=False, extend_table=None, return_value=NIL, return_flag=False):
        self._tree = tree
        self.var_table = {}  # variable table
        if tb is not None:
            self.var_table.update(tb)
        if extend_table is not None:
            self.var_table.update(extend_table)
        self.loop_flag = loop  # 循环内指示器，大于0为循环层数，等于0为不在循环内，小于0非法
        self.break_flag = break_flag  # break指示器
        self.return_value = return_value  # 返回值
        self.return_flag = return_flag  # 返回标志

    def _save(self, tran):
        self.var_table = tran.var_table
        self.loop_flag = tran.loop_flag
        self.break_flag = tran.break_flag
        self.return_value = tran.return_value
        self.return_flag = tran.return_flag

    def translate(self):
        if self.break_flag or self.return_flag:
            return self.return_value
        # 提前翻译 if for while function class
        if isinstance(self._tree, NonTerminal):
            # Function
            if self._tree.type == 'Function':
                """function : DEF ID LPAREN args RPAREN LBRACE statements RBRACE
                            | DEF ID LPAREN RPAREN LBRACE statements RBRACE"""
                name = self._tree.child(1).id
                if len(self._tree.children) == 8:
                    tran = Translator(self._tree.child(3), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag,
                                      return_value=self.return_value, return_flag=self.return_flag)
                    tran.translate()
                    self._save(tran)
                    args = self._tree.child(3).value
                    body = self._tree.child(6)
                else:
                    args = []
                    body = self._tree.child(5)
                func = Function(name, args, body)
                self.var_table[name] = func
                return self.return_value
            # Class
            elif self._tree.type == 'Class':
                """class : CLASS ID LBRACE functions RBRACE"""
                name = self._tree.child(1).id
                body = self._tree.child(3)
                cls = Class(name, body)
                self.var_table[name] = cls
                return self.return_value
            # If
            elif self._tree.type == 'If':
                """if : IF LPAREN condition RPAREN LBRACE statements RBRACE"""
                tran = Translator(self._tree.child(2), tb=self.var_table,
                                  loop=self.loop_flag, break_flag=self.break_flag)  # Condition
                tran.translate()
                self._save(tran)
                condition = self._tree.child(2).value
                if condition:
                    tran = Translator(self._tree.child(5), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Statements
                    tran.translate()
                    self._save(tran)
                    # if len(self._tree.children) == 8:
                    #     self._tree.children.pop(-1)
                else:
                    if len(self._tree.children) == 8:
                        tran = Translator(self._tree.child(7), tb=self.var_table,
                                          loop=self.loop_flag, break_flag=self.break_flag)  # `else`
                        tran.translate()
                        self._save(tran)
                return self.return_value
            # Else
            elif self._tree.type == 'Else':
                if len(self._tree.children) == 4:
                    """ELSE LBRACE statements2 RBRACE"""
                    tran = Translator(self._tree.child(2), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Statements2
                    tran.translate()
                    self._save(tran)
                elif 7 <= len(self._tree.children) <= 8:
                    """ELIF LPAREN condition RPAREN LBRACE statements RBRACE
                     | ELIF LPAREN condition RPAREN LBRACE statements RBRACE else"""
                    tran = Translator(self._tree.child(2), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Condition2
                    tran.translate()
                    self._save(tran)
                    elif_condition = self._tree.child(2).value
                    if elif_condition:
                        tran = Translator(self._tree.child(5), tb=self.var_table,
                                          loop=self.loop_flag, break_flag=self.break_flag)  # Statements2
                        tran.translate()
                        self._save(tran)
                    else:
                        if len(self._tree.children) == 8:
                            tran = Translator(self._tree.child(7), tb=self.var_table,
                                              loop=self.loop_flag, break_flag=self.break_flag)  # `else`
                            tran.translate()
                            self._save(tran)
                return self.return_value
            elif self._tree.type == 'While':
                """while : WHILE LPAREN condition RPAREN LBRACE statements RBRACE"""
                _loop_count = 0
                self.loop_flag += 1  # 进入一层循环
                while True:
                    tran = Translator(self._tree.child(2), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Condition
                    tran.translate()
                    self._save(tran)
                    condition = self._tree.child(2).value
                    if not condition:
                        self.loop_flag -= 1  # 跳出一层循环
                        break
                    tran = Translator(self._tree.child(5), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Statements
                    tran.translate()
                    self._save(tran)
                    if self.break_flag:
                        self.break_flag = False  # 执行break
                        self.loop_flag -= 1  # 跳出一层循环
                        break
                return self.return_value
            # For
            elif self._tree.type == 'For':
                """for : FOR LPAREN assignment SEMICOLON condition SEMICOLON assignment RPAREN LBRACE statements RBRACE"""
                _loop_count = 0
                tran = Translator(self._tree.child(2), tb=self.var_table,
                                  loop=self.loop_flag, break_flag=self.break_flag,
                                  return_value=self.return_value, return_flag=self.return_flag)  # Assignment
                tran.translate()
                self._save(tran)
                self.loop_flag += 1  # 进入一层循环
                while True:
                    tran = Translator(self._tree.child(4), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag,
                                      return_value=self.return_value, return_flag=self.return_flag)  # Condition
                    tran.translate()
                    self._save(tran)
                    condition = self._tree.child(4).value
                    if not condition:
                        self.loop_flag -= 1
                        break
                    tran = Translator(self._tree.child(9), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag,
                                      return_value=self.return_value, return_flag=self.return_flag)  # Statements
                    tran.translate()
                    self._save(tran)
                    if self.break_flag:
                        self.break_flag = False  # 执行break
                        self.loop_flag -= 1  # 跳出一层循环
                        break
                    tran = Translator(self._tree.child(6), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag,
                                      return_value=self.return_value, return_flag=self.return_flag)  # Assignment
                    tran.translate()
                    self._save(tran)
                return self.return_value
            # Break
            elif self._tree.type == 'Break':
                self.break_flag = True  # 转为break状态
                return self.return_value
            # Return
            elif self._tree.type == 'Return':
                if len(self._tree.children) == 2:
                    val = self._tree.child(1).value
                    if len(val) == 1:
                        val = val[0]
                else:
                    val = None
                self.return_value = val
                self.return_flag = True
                return self.return_value

        for child in self._tree.children:
            tran = Translator(child, tb=self.var_table,
                              loop=self.loop_flag, break_flag=self.break_flag,
                              return_value=self.return_value, return_flag=self.return_flag)
            tran.translate()
            self._save(tran)

        # Translation
        if isinstance(self._tree, NonTerminal):
            # Assignment
            if self._tree.type == 'Assignment':
                '''assignment : variable ASSIGN expr
                              | variable MINEQUAL expr
                              | variable PLUSEQUAL expr
                              | variable DPLUS
                              | variable DMINUS'''
                if len(self._tree.children) == 3:
                    if self._tree.child(1).text == '=':
                        value = self._tree.child(2).value
                    else:
                        value = self.get_value(self.var_table, self._tree.child(0).id)
                        if self._tree.child(1).text == '+=':
                            value += self._tree.child(2).value
                        elif self._tree.child(1).text == '-=':
                            value -= self._tree.child(2).value
                    self.set_value(self.var_table, self._tree.child(0).id, value)
                elif len(self._tree.children) == 2:
                    value = self.get_value(self.var_table, self._tree.child(0).id)
                    if self._tree.child(1).text == '++':
                        value += 1
                    elif self._tree.child(1).text == '--':
                        value -= 1
                    self.set_value(self.var_table, self._tree.child(0).id, value)  # update var_table
            elif self._tree.type == 'Variable':
                """variable : variable LBRACKET expr RBRACKET | ID | ID DOT ID"""
                if len(self._tree.children) == 1:
                    self._tree.id = (self._tree.child(0).id, None)
                    if self._tree.child(0).value is not NIL:
                        self.set_value(self.var_table, self._tree.id, self._tree.child(0).value)
                elif len(self._tree.children) == 4:
                    self._tree.id = (self._tree.child(0).id, self._tree.child(2).value)
                elif len(self._tree.children) == 3:
                    obj_id = self._tree.child(0).id
                    prop = self._tree.child(2).id
                    self._tree.id = (obj_id, prop)
            # Expr
            elif self._tree.type == 'Expr':
                '''expr : expr '+' term | expr '-' term | term | array | string'''
                if len(self._tree.children) == 1:
                    self._tree.value = self._tree.child(0).value
                elif len(self._tree.children) == 3:
                    op = self._tree.child(1).text
                    if op == '+':
                        value = self._tree.child(0).value + self._tree.child(2).value
                    else:
                        value = self._tree.child(0).value - self._tree.child(2).value
                    self._tree.value = value
            # Term
            elif self._tree.type == 'Term':
                '''term : term '*' factor | term '/' factor | factor'''
                if len(self._tree.children) == 1:
                    self._tree.value = self._tree.child(0).value
                elif len(self._tree.children) == 3:
                    op = self._tree.child(1).text
                    if op == '*':
                        value = self._tree.child(0).value * self._tree.child(2).value
                    else:
                        if op == '//':
                            value = self._tree.child(0).value // self._tree.child(2).value
                        else:
                            value = self._tree.child(0).value / self._tree.child(2).value
                    self._tree.value = value
            # Factor
            elif self._tree.type == 'Factor':
                """factor : variable | NUMBER | len | call | '(' expr ')'"""
                if len(self._tree.children) == 1:
                    if isinstance(self._tree.child(0), Variable):  # variable
                        value = self.get_value(self.var_table, self._tree.child(0).id)  # search for var_table
                        assert value is not None, f'符号 "{self._tree.child(0).id}" 未定义'
                        self._tree.value = value
                    elif isinstance(self._tree.child(0), NonTerminal):
                        self._tree.value = self._tree.child(0).value
                    else:
                        self._tree.value = self._tree.child(0).value
                elif len(self._tree.children) == 3:
                    self._tree.value = self._tree.child(1).value
            # Exprs
            elif self._tree.type == 'Exprs':
                """exprs : exprs ',' expr | expr"""
                if len(self._tree.children) == 1:
                    self._tree.value = [self._tree.child(0).value]
                elif len(self._tree.children) == 3:
                    self._tree.value = self._tree.child(0).value + [self._tree.child(2).value]
            # Print
            elif self._tree.type == 'Print':
                ''' print : PRINT '(' exprs ')' | PRINT '(' ')' '''
                if len(self._tree.children) == 4:
                    print(*self._tree.child(2).value)
                else:
                    print()
            # Len
            elif self._tree.type == 'Len':
                """len -> LEN '(' variable ')'  { len.value = len(variable.value) }"""
                value = self.get_value(self.var_table, self._tree.child(2).id)
                self._tree.value = len(value)
            # Array
            elif self._tree.type == 'Array':
                ''' array : '[' exprs ']' | '[' ']' '''
                if len(self._tree.children) == 3:
                    self._tree.value = list(self._tree.child(1).value)
                else:
                    self._tree.value = []
            # String
            elif self._tree.type == 'String':
                ''' string : STRING '''
                self._tree.value = self._tree.child(0).value
            # Condition
            elif self._tree.type == 'Condition':
                """ condition : condition OR join | join """
                if len(self._tree.children) == 3:
                    self._tree.value = self._tree.child(0).value or self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    self._tree.value = self._tree.child(0).value
            # Join
            elif self._tree.type == 'Join':
                """ join : join AND equality | equality """
                if len(self._tree.children) == 3:
                    self._tree.value = self._tree.child(0).value and self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    self._tree.value = self._tree.child(0).value
            # Equality
            elif self._tree.type == 'Equality':
                """ equality : equality EQ rel | equality NE rel | rel
                    rel : expr LT expr | expr LE expr | expr GT expr | expr GE expr | expr """
                if len(self._tree.children) == 3:
                    if self._tree.child(1).text == '==':
                        self._tree.value = self._tree.child(0).value == self._tree.child(2).value
                    elif self._tree.child(1).text == '!=':
                        self._tree.value = self._tree.child(0).value != self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    self._tree.value = self._tree.child(0).value
            # Relation
            elif self._tree.type == 'Relation':
                """ rel : expr LT expr | expr LE expr | expr GT expr | expr GE expr | expr """
                if len(self._tree.children) == 3:
                    if self._tree.child(1).text == '<':
                        self._tree.value = self._tree.child(0).value < self._tree.child(2).value
                    elif self._tree.child(1).text == '<=':
                        self._tree.value = self._tree.child(0).value <= self._tree.child(2).value
                    elif self._tree.child(1).text == '>':
                        self._tree.value = self._tree.child(0).value > self._tree.child(2).value
                    elif self._tree.child(1).text == '>=':
                        self._tree.value = self._tree.child(0).value >= self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    self._tree.value = bool(self._tree.child(0).value)
            # Args
            elif self._tree.type == 'Args':
                """args : args COMMA ID | ID"""
                if len(self._tree.children) == 1:
                    self._tree.value = [self._tree.child(0).id]
                elif len(self._tree.children) == 3:
                    self._tree.value = self._tree.child(0).value + [self._tree.child(2).id]
            # Call
            elif self._tree.type == 'Call':
                if 3 <= len(self._tree.children) <= 4:
                    """call : ID LPAREN exprs RPAREN | ID LPAREN RPAREN"""
                    if len(self._tree.children) == 4:
                        args = self._tree.child(2).value
                    else:
                        args = []
                    # print(args)
                    func = self.get_value(self.var_table, (self._tree.child(0).id, None))
                    if isinstance(func, Function):
                        self._tree.value, _ = func.exec(self, args)
                    else:
                        obj = PyObject(func)
                        obj.constructor(args=args)
                        self._tree.value = obj
                elif 5 <= len(self._tree.children) <= 6:
                    """call : ID DOT ID LPAREN exprs RPAREN | ID DOT ID LPAREN RPAREN"""
                    this = self.get_value(self.var_table, (self._tree.child(0).id, None))
                    if len(self._tree.children) == 6:
                        args = [this] + self._tree.child(4).value
                    else:
                        args = [this]
                    # print(args)
                    func = this[self._tree.child(2).id]
                    if isinstance(func, Function):
                        self._tree.value, _ = func.exec(self, args)
                    else:
                        obj = PyObject(func)
                        obj.constructor(args=args)
                        self._tree.value = obj

        return self.return_value
