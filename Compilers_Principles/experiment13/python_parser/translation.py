# coding=utf-8
from node import *

DEBUG_MODE = False  # 调试时输出部分运行信息


class Function:
    def __init__(self, name, arg_names, body):
        self.name = name
        self.arg_names = arg_names
        self.body = body

    def __repr__(self):
        return f"<Function object '{self.name}'>"

    def exec(self, env, args):
        etb = {self.name: self}
        for k, v in zip(self.arg_names, args):
            etb[k] = v
        if DEBUG_MODE: print(etb)
        if env is None:
            tran = Translator(self.body, extend_table=etb)
        else:
            tran = Translator(self.body, tb=env.var_table, extend_table=etb)
        ret = tran.translate()
        return ret, tran


class Class:
    def __init__(self, name, funcs):
        self.name = name
        tran = Translator(funcs)
        tran.translate()
        self.functions = tran.var_table

    def __repr__(self):
        return f"<Class object '{self.name}'>"


class PyObject:
    def __init__(self, cls):
        self.cls = cls
        self.props = {}
        self.props.update(self.cls.functions)

    def __repr__(self):
        address = hex(id(self))
        return f"<PyObject {self.cls.name} at {address}>"

    def constructor(self, args):
        if self.cls.functions.get('__init__', None) is None:
            assert len(args) == 0, "default constructor doesn't need argument(s)!"
            return
        _, tran = self.cls.functions['__init__'].exec(env=None, args=[self] + args)
        for name, value in tran.var_table.items():
            self.props[name] = value

    def __getitem__(self, item):
        assert isinstance(item, str)
        if self.props.get(item, None) is None:
            raise AttributeError(f"'{self.cls.name}' object has no attribute '{item}'")
        return self.props[item]

    def __setitem__(self, key, value):
        assert isinstance(key, str)
        self.props[key] = value


class Translator:

    @staticmethod
    def get_value(tb, vid):
        name, sub = vid
        if DEBUG_MODE: print(name, sub)
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
                assert (len(self._tree.children) == 8 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'def' and
                        isinstance(self._tree.child(1), ID) and
                        isinstance(self._tree.child(2), Terminal) and self._tree.child(2).text == '(' and
                        isinstance(self._tree.child(3), NonTerminal) and self._tree.child(3).type == 'Args' and
                        isinstance(self._tree.child(4), Terminal) and self._tree.child(4).text == ')' and
                        isinstance(self._tree.child(5), Terminal) and self._tree.child(5).text == '{' and
                        isinstance(self._tree.child(6), NonTerminal) and self._tree.child(6).type == 'Statements' and
                        isinstance(self._tree.child(7), Terminal) and self._tree.child(7).text == '}') or \
                       (len(self._tree.children) == 7 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'def' and
                        isinstance(self._tree.child(1), ID) and
                        isinstance(self._tree.child(2), Terminal) and self._tree.child(1).text == '(' and
                        isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')' and
                        isinstance(self._tree.child(4), Terminal) and self._tree.child(4).text == '{' and
                        isinstance(self._tree.child(5), NonTerminal) and self._tree.child(5).type == 'Statements' and
                        isinstance(self._tree.child(6), Terminal) and self._tree.child(6).text == '}'), 'Syntax error'
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
                assert len(self._tree.children) == 5 and \
                       isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'class' and \
                       isinstance(self._tree.child(1), ID) and \
                       isinstance(self._tree.child(2), Terminal) and self._tree.child(2).text == '{' and \
                       isinstance(self._tree.child(3), NonTerminal) and self._tree.child(3).type == 'Functions' and \
                       isinstance(self._tree.child(4), Terminal) and \
                       self._tree.child(4).text == '}', 'Syntax error'
                name = self._tree.child(1).id
                body = self._tree.child(3)
                cls = Class(name, body)
                self.var_table[name] = cls
                return self.return_value
            # If
            elif self._tree.type == 'If':
                """if : IF LPAREN condition RPAREN LBRACE statements RBRACE"""
                assert 7 <= len(self._tree.children) <= 8, 'Syntax error'
                assert isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'if' and \
                       isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and \
                       isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Condition' and \
                       isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')' and \
                       isinstance(self._tree.child(4), Terminal) and self._tree.child(4).text == '{' and \
                       isinstance(self._tree.child(5), NonTerminal) and self._tree.child(5).type == 'Statements' and \
                       isinstance(self._tree.child(6), Terminal) and self._tree.child(6).text == '}', 'Syntax error'
                if len(self._tree.children) == 8:
                    assert isinstance(self._tree.child(7), NonTerminal) and \
                           self._tree.child(7).type == 'Else', 'Syntax error'
                if DEBUG_MODE: print('if (...)')
                tran = Translator(self._tree.child(2), tb=self.var_table,
                                  loop=self.loop_flag, break_flag=self.break_flag)  # Condition
                tran.translate()
                self._save(tran)
                condition = self._tree.child(2).value
                if condition:
                    if DEBUG_MODE: print('then {...}  # if-then')
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
                assert len(self._tree.children) in (4, 7, 8), 'Syntax error'
                if len(self._tree.children) == 4:
                    """ELSE LBRACE statements2 RBRACE"""
                    assert isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'else' and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '{' and \
                           isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Statements' and \
                           isinstance(self._tree.child(3), Terminal) and \
                           self._tree.child(3).text == '}', 'Syntax error'
                    if DEBUG_MODE: print('else {...}  # else')
                    tran = Translator(self._tree.child(2), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Statements2
                    tran.translate()
                    self._save(tran)
                elif 7 <= len(self._tree.children) <= 8:
                    """ELIF LPAREN condition RPAREN LBRACE statements RBRACE
                     | ELIF LPAREN condition RPAREN LBRACE statements RBRACE else"""
                    assert isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'elif' and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and \
                           isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Condition' and \
                           isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')' and \
                           isinstance(self._tree.child(4), Terminal) and self._tree.child(4).text == '{' and \
                           isinstance(self._tree.child(5), NonTerminal) and self._tree.child(5).type == 'Statements' and \
                           isinstance(self._tree.child(6), Terminal) and self._tree.child(6).text == '}', 'Syntax error'
                    if DEBUG_MODE: print('elif (...)')
                    tran = Translator(self._tree.child(2), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Condition2
                    tran.translate()
                    self._save(tran)
                    elif_condition = self._tree.child(2).value
                    if elif_condition:
                        if DEBUG_MODE: print('then {...}  # elif-then')
                        tran = Translator(self._tree.child(5), tb=self.var_table,
                                          loop=self.loop_flag, break_flag=self.break_flag)  # Statements2
                        tran.translate()
                        self._save(tran)
                    else:  # 只有elif没有成立才执行
                        if len(self._tree.children) == 8:
                            tran = Translator(self._tree.child(7), tb=self.var_table,
                                              loop=self.loop_flag, break_flag=self.break_flag)  # `else`
                            tran.translate()
                            self._save(tran)
                return self.return_value
            # While
            elif self._tree.type == 'While':
                """while : WHILE LPAREN condition RPAREN LBRACE statements RBRACE"""
                assert len(self._tree.children) == 7 and \
                       isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'while' and \
                       isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and \
                       isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Condition' and \
                       isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')' and \
                       isinstance(self._tree.child(4), Terminal) and self._tree.child(4).text == '{' and \
                       isinstance(self._tree.child(5), NonTerminal) and self._tree.child(5).type == 'Statements' and \
                       isinstance(self._tree.child(6), Terminal) and self._tree.child(6).text == '}', 'Syntax error'
                if DEBUG_MODE: print('while (...)')
                _loop_count = 0
                self.loop_flag += 1  # 进入一层循环
                while True:
                    tran = Translator(self._tree.child(2), tb=self.var_table,
                                      loop=self.loop_flag, break_flag=self.break_flag)  # Condition
                    tran.translate()
                    self._save(tran)
                    condition = self._tree.child(2).value
                    if not condition:
                        if DEBUG_MODE: print('# end-while')
                        self.loop_flag -= 1  # 跳出一层循环
                        break
                    if DEBUG_MODE:
                        print('do {...}  # while, count =', (_loop_count := _loop_count + 1),
                              'indent =', self.loop_flag)
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
                assert len(self._tree.children) == 11 and \
                       isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'for' and \
                       isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and \
                       isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Assignment' and \
                       isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ';' and \
                       isinstance(self._tree.child(4), NonTerminal) and self._tree.child(4).type == 'Condition' and \
                       isinstance(self._tree.child(5), Terminal) and self._tree.child(5).text == ';' and \
                       isinstance(self._tree.child(6), NonTerminal) and self._tree.child(6).type == 'Assignment' and \
                       isinstance(self._tree.child(7), Terminal) and self._tree.child(7).text == ')' and \
                       isinstance(self._tree.child(8), Terminal) and self._tree.child(8).text == '{' and \
                       isinstance(self._tree.child(9), NonTerminal) and self._tree.child(9).type == 'Statements' and \
                       isinstance(self._tree.child(10), Terminal) and self._tree.child(10).text == '}', 'Syntax error'
                if DEBUG_MODE: print('for (...;...;...)')
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
                        if DEBUG_MODE: print('# end-for')
                        self.loop_flag -= 1  # 跳出一层循环
                        break
                    if DEBUG_MODE:
                        print('do {...}  # for, count =', (_loop_count := _loop_count + 1),
                              'indent =', self.loop_flag)
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
                assert len(self._tree.children) == 1 and \
                       isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'break', 'Syntax error'
                assert self.loop_flag > 0, 'Syntax error: use "break" in non-loop statements'
                self.break_flag = True  # 转为break状态
                if DEBUG_MODE: print('BREAK!')
                return self.return_value
            # Return
            elif self._tree.type == 'Return':
                assert (len(self._tree.children) == 1 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'return') or \
                       (len(self._tree.children) == 2 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'return' and
                        isinstance(self._tree.child(1), NonTerminal) and
                        self._tree.child(1).type == 'Exprs'), 'Syntax error'
                if len(self._tree.children) == 2:
                    val = self._tree.child(1).value
                    if len(val) == 1:
                        val = val[0]
                else:
                    val = None
                self.return_value = val
                self.return_flag = True
                if DEBUG_MODE: print('!!return', val)
                return self.return_value

        # 深度优先遍历语法树
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
                assert (len(self._tree.children) == 3 and
                        isinstance(self._tree.child(0), Variable) and
                        isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text in ('=', '+=', '-=') and
                        isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Expr') or \
                       (len(self._tree.children) == 2 and
                        isinstance(self._tree.child(0), Variable) and
                        isinstance(self._tree.child(1), Terminal) and
                        self._tree.child(1).text in ('++', '--')), 'Syntax error'
                if len(self._tree.children) == 3:
                    if self._tree.child(1).text == '=':
                        value = self._tree.child(2).value
                    else:
                        value = self.get_value(self.var_table, self._tree.child(0).id)
                        if self._tree.child(1).text == '+=':
                            value += self._tree.child(2).value
                        elif self._tree.child(1).text == '-=':
                            value -= self._tree.child(2).value
                    self.set_value(self.var_table, self._tree.child(0).id, value)  # update var_table
                    if DEBUG_MODE: print('assignment', self._tree.child(0).id, value)
                elif len(self._tree.children) == 2:
                    value = self.get_value(self.var_table, self._tree.child(0).id)
                    if self._tree.child(1).text == '++':
                        value += 1
                    elif self._tree.child(1).text == '--':
                        value -= 1
                    self.set_value(self.var_table, self._tree.child(0).id, value)  # update var_table
                    if DEBUG_MODE: print('SelfVar', self._tree.child(0).id, self._tree.child(1).text, value)
            # Variable
            elif self._tree.type == 'Variable':
                """variable : variable LBRACKET expr RBRACKET | ID | ID DOT ID"""
                assert len(self._tree.children) in (1, 3, 4), 'Syntax error'
                if len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), ID), 'Syntax error'
                    self._tree.id = (self._tree.child(0).id, None)
                    if self._tree.child(0).value is not NIL:
                        self.set_value(self.var_table, self._tree.id, self._tree.child(0).value)
                        if DEBUG_MODE: print('assignment', self._tree.id, self._tree.child(0).value)
                elif len(self._tree.children) == 4:
                    assert isinstance(self._tree.child(0), Variable) and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '[' and \
                           isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Expr' and \
                           isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ']', 'Syntax error'
                    self._tree.id = (self._tree.child(0).id, self._tree.child(2).value)
                elif len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), ID) and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '.' and \
                           isinstance(self._tree.child(2), ID), 'Syntax error'
                    obj_id = self._tree.child(0).id
                    prop = self._tree.child(2).id
                    self._tree.id = (obj_id, prop)
            # Expr
            elif self._tree.type == 'Expr':
                '''expr : expr '+' term | expr '-' term | term | array | string'''
                assert len(self._tree.children) == 1 or len(self._tree.children) == 3, 'Syntax error'
                if len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type in ('Term', 'Array', 'String'), 'Syntax error'
                    self._tree.value = self._tree.child(0).value
                elif len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and self._tree.child(0).type == 'Expr' and \
                           isinstance(self._tree.child(1), Terminal) and (self._tree.child(1).text in ('+', '-')) and \
                           isinstance(self._tree.child(2), NonTerminal) and \
                           self._tree.child(2).type == 'Term', 'Syntax error'
                    op = self._tree.child(1).text
                    if op == '+':
                        value = self._tree.child(0).value + self._tree.child(2).value
                    else:
                        value = self._tree.child(0).value - self._tree.child(2).value
                    self._tree.value = value
            # Term
            elif self._tree.type == 'Term':
                '''term : term '*' factor | term '/' factor | factor'''
                assert len(self._tree.children) == 1 or len(self._tree.children) == 3, 'Syntax error'
                if len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and self._tree.child(
                        0).type == 'Factor', 'Syntax error'
                    self._tree.value = self._tree.child(0).value
                elif len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and self._tree.child(0).type == 'Term' and \
                           isinstance(self._tree.child(1), Terminal) and \
                           (self._tree.child(1).text in ('*', '/', '//')) and \
                           isinstance(self._tree.child(2), NonTerminal) and self._tree.child(
                        2).type == 'Factor', 'Syntax error'
                    op = self._tree.child(1).text
                    if op == '*':
                        value = self._tree.child(0).value * self._tree.child(2).value
                    else:
                        assert self._tree.child(2).value != 0, '除数不能为0'
                        if op == '//':
                            value = self._tree.child(0).value // self._tree.child(2).value
                        else:
                            value = self._tree.child(0).value / self._tree.child(2).value
                    self._tree.value = value
            # Factor
            elif self._tree.type == 'Factor':
                """factor : variable | NUMBER | len | call | '(' expr ')'"""
                assert len(self._tree.children) == 1 or len(self._tree.children) == 3, 'Syntax error'
                if len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), Variable) or \
                           isinstance(self._tree.child(0), Number) or \
                           (isinstance(self._tree.child(0), NonTerminal) and self._tree.child(0).type == 'Len') or \
                           (isinstance(self._tree.child(0), NonTerminal) and
                            self._tree.child(0).type == 'Call'), 'Syntax error'
                    if isinstance(self._tree.child(0), Variable):  # variable
                        value = self.get_value(self.var_table, self._tree.child(0).id)  # search for var_table
                        assert value is not None, f'符号 "{self._tree.child(0).id}" 未定义'
                        self._tree.value = value
                    elif isinstance(self._tree.child(0), NonTerminal):
                        self._tree.value = self._tree.child(0).value
                    else:
                        self._tree.value = self._tree.child(0).value
                elif len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == '(' and \
                           isinstance(self._tree.child(1), NonTerminal) and self._tree.child(1).type == 'Expr' and \
                           isinstance(self._tree.child(2), Terminal) and self._tree.child(2).text == ')', 'Syntax error'
                    self._tree.value = self._tree.child(1).value
            # Exprs
            elif self._tree.type == 'Exprs':
                """exprs : exprs ',' expr | expr"""
                assert len(self._tree.children) == 1 or len(self._tree.children) == 3, 'Syntax error'
                if len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Expr', 'Syntax error'
                    self._tree.value = [self._tree.child(0).value]
                elif len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and self._tree.child(0).type == 'Exprs' and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == ',' and \
                           isinstance(self._tree.child(2), NonTerminal) and \
                           self._tree.child(2).type == 'Expr', 'Syntax error'
                    self._tree.value = self._tree.child(0).value + [self._tree.child(2).value]
            # Print
            elif self._tree.type == 'Print':
                ''' print : PRINT '(' exprs ')' | PRINT '(' ')' '''
                assert (len(self._tree.children) == 4 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'print' and
                        isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and
                        isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Exprs' and
                        isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')') or \
                       (len(self._tree.children) == 3 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'print' and
                        isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and
                        isinstance(self._tree.child(2), Terminal) and self._tree.child(2).text == ')'), 'Syntax error'
                if len(self._tree.children) == 4:
                    print(*self._tree.child(2).value)
                else:
                    print()
            # Len
            elif self._tree.type == 'Len':
                """len -> LEN '(' variable ')'  { len.value = len(variable.value) }"""
                assert len(self._tree.children) == 4 and \
                       isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == 'len' and \
                       isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and \
                       isinstance(self._tree.child(2), Variable) and \
                       isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')', 'Syntax error'
                value = self.get_value(self.var_table, self._tree.child(2).id)
                self._tree.value = len(value)
            # Array
            elif self._tree.type == 'Array':
                ''' array : '[' exprs ']' | '[' ']' '''
                assert (len(self._tree.children) == 3 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == '[' and
                        isinstance(self._tree.child(1), NonTerminal) and self._tree.child(1).type == 'Exprs' and
                        isinstance(self._tree.child(2), Terminal) and self._tree.child(2).text == ']') or \
                       (len(self._tree.children) == 2 and
                        isinstance(self._tree.child(0), Terminal) and self._tree.child(0).text == '[' and
                        isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == ']'), 'Syntax error'
                if len(self._tree.children) == 3:
                    self._tree.value = list(self._tree.child(1).value)
                else:
                    self._tree.value = []
            # String
            elif self._tree.type == 'String':
                ''' string : STRING '''
                assert len(self._tree.children) == 1 and isinstance(self._tree.child(0), String), 'Syntax error'
                self._tree.value = self._tree.child(0).value
            # Condition
            elif self._tree.type == 'Condition':
                """ condition : condition OR join | join """
                assert len(self._tree.children) == 3 or len(self._tree.children) == 1, 'Syntax error'
                if len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Condition' and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == 'or' and \
                           isinstance(self._tree.child(2), NonTerminal) and \
                           self._tree.child(2).type == 'Join', 'Syntax error'
                    self._tree.value = self._tree.child(0).value or self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Join', 'Syntax error'
                    self._tree.value = self._tree.child(0).value
            # Join
            elif self._tree.type == 'Join':
                """ join : join AND equality | equality """
                assert len(self._tree.children) == 3 or len(self._tree.children) == 1, 'Syntax error'
                if len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Join' and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == 'and' and \
                           isinstance(self._tree.child(2), NonTerminal) and \
                           self._tree.child(2).type == 'Equality', 'Syntax error'
                    self._tree.value = self._tree.child(0).value and self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Equality', 'Syntax error'
                    self._tree.value = self._tree.child(0).value
            # Equality
            elif self._tree.type == 'Equality':
                """ equality : equality EQ rel | equality NE rel | rel
                    rel : expr LT expr | expr LE expr | expr GT expr | expr GE expr | expr """
                assert len(self._tree.children) == 3 or len(self._tree.children) == 1, 'Syntax error'
                if len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Equality' and \
                           isinstance(self._tree.child(1), Terminal) and \
                           self._tree.child(1).text in ('==', '!=') and \
                           isinstance(self._tree.child(2), NonTerminal) and \
                           self._tree.child(2).type == 'Relation', 'Syntax error'
                    if self._tree.child(1).text == '==':
                        self._tree.value = self._tree.child(0).value == self._tree.child(2).value
                    elif self._tree.child(1).text == '!=':
                        self._tree.value = self._tree.child(0).value != self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Relation', 'Syntax error'
                    self._tree.value = self._tree.child(0).value
            # Relation
            elif self._tree.type == 'Relation':
                """ rel : expr LT expr | expr LE expr | expr GT expr | expr GE expr | expr """
                assert len(self._tree.children) == 3 or len(self._tree.children) == 1, 'Syntax error'
                if len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Expr' and \
                           isinstance(self._tree.child(1), Terminal) and \
                           self._tree.child(1).text in ('<', '<=', '>', '>=') and \
                           isinstance(self._tree.child(2), NonTerminal) and \
                           self._tree.child(2).type == 'Expr', 'Syntax error'
                    if self._tree.child(1).text == '<':
                        self._tree.value = self._tree.child(0).value < self._tree.child(2).value
                    elif self._tree.child(1).text == '<=':
                        self._tree.value = self._tree.child(0).value <= self._tree.child(2).value
                    elif self._tree.child(1).text == '>':
                        self._tree.value = self._tree.child(0).value > self._tree.child(2).value
                    elif self._tree.child(1).text == '>=':
                        self._tree.value = self._tree.child(0).value >= self._tree.child(2).value
                elif len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), NonTerminal) and \
                           self._tree.child(0).type == 'Expr', 'Syntax error'
                    self._tree.value = bool(self._tree.child(0).value)
                if DEBUG_MODE: print('condition:', self._tree.value)
            # Args
            elif self._tree.type == 'Args':
                """args : args COMMA ID | ID"""
                assert len(self._tree.children) == 1 or len(self._tree.children) == 3, 'Syntax error'
                if len(self._tree.children) == 1:
                    assert isinstance(self._tree.child(0), ID), 'Syntax error'
                    self._tree.value = [self._tree.child(0).id]
                elif len(self._tree.children) == 3:
                    assert isinstance(self._tree.child(0), NonTerminal) and self._tree.child(0).type == 'Args' and \
                           isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == ',' and \
                           isinstance(self._tree.child(2), ID), 'Syntax error'
                    self._tree.value = self._tree.child(0).value + [self._tree.child(2).id]
            # Call
            elif self._tree.type == 'Call':
                if 3 <= len(self._tree.children) <= 4:
                    """call : ID LPAREN exprs RPAREN | ID LPAREN RPAREN"""
                    assert (len(self._tree.children) == 4 and
                            isinstance(self._tree.child(0), ID) and
                            isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and
                            isinstance(self._tree.child(2), NonTerminal) and self._tree.child(2).type == 'Exprs' and
                            isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == ')') or \
                           (len(self._tree.children) == 3 and
                            isinstance(self._tree.child(0), ID) and
                            isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '(' and
                            isinstance(self._tree.child(2), Terminal) and
                            self._tree.child(2).text == ')'), 'Syntax error'
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
                    assert (len(self._tree.children) == 6 and
                            isinstance(self._tree.child(0), ID) and
                            isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '.' and
                            isinstance(self._tree.child(2), ID) and
                            isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == '(' and
                            isinstance(self._tree.child(4), NonTerminal) and self._tree.child(4).type == 'Exprs' and
                            isinstance(self._tree.child(5), Terminal) and self._tree.child(5).text == ')') or \
                           (len(self._tree.children) == 5 and
                            isinstance(self._tree.child(0), ID) and
                            isinstance(self._tree.child(1), Terminal) and self._tree.child(1).text == '.' and
                            isinstance(self._tree.child(2), ID) and
                            isinstance(self._tree.child(3), Terminal) and self._tree.child(3).text == '(' and
                            isinstance(self._tree.child(4), Terminal) and
                            self._tree.child(4).text == ')'), 'Syntax error'
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
