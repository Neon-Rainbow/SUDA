# coding=utf-8
import re
import threading


class _node:
    """
    所有节点的基类
    """

    def __init__(self, data):
        self._data = data
        self._children = []
        self._value = NIL

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def child(self, i):
        assert -len(self._children) <= i < len(self._children), f'{i}'
        return self._children[i]

    @property
    def children(self):
        return self._children

    def add(self, node):
        self._children.append(node)


class NonTerminal(_node):
    """
    非终结符节点，提供type表示非终结符的类型，value（可选）为值
    """

    @property
    def type(self):
        return self._data

    def __str__(self):
        if len(self.children) == 0:
            children = ''
        else:
            children = ' ' + ' '.join(map(str, self.children))
        r = f"[{self.type}{children}]"
        return re.sub(r'\s+', ' ', r)


class Variable(NonTerminal):
    """
    左值节点，提供type表示非终结符的类型，id表示引用的变量
    """

    def __init__(self, data):
        super(Variable, self).__init__(data)
        self._id = None
        del self._value

    def __str__(self):
        if len(self.children) == 0:
            children = ''
        else:
            children = ' ' + ' '.join(map(str, self.children))
        r = f"[{self.type}{children}]"
        return re.sub(r'\s+', ' ', r)

    @property
    def id(self):
        return self._id

    @property
    def value(self):
        raise ValueError('Variable 的 value 属性不被允许使用，请通过检索符号表实现')

    @id.setter
    def id(self, i):
        self._id = i


class Number(_node):
    """
    数字节点，value为值
    """

    def __init__(self, data):
        super(Number, self).__init__(data)
        self._data = 'number'
        self._value = int(data)

    def __str__(self):
        return f'Number({self._value})'


class String(_node):
    """
    字符串节点，value为值
    """

    def __init__(self, data):
        super(String, self).__init__(data)
        self._data = 'string'
        self._value = str(data[1:-1])

    def __str__(self):
        return f'String("{self._value}")'


class ID(_node):
    """
    标识符节点，提供id表示标识符名称，value为值
    """

    @property
    def id(self):
        return self._data

    def __init__(self, data):
        super(ID, self).__init__(data)
        self._value = NIL

    def __str__(self):
        id_ = self._data
        return f"ID('{id_}')"


class Terminal(_node):
    """
    除标识符以外的终结符节点，提供text表示其内容
    """

    @property
    def text(self):
        return self._data

    def __str__(self):
        s = str(self._data).replace('<=', '≤').replace('>=', '≥').replace('<', '＜').replace('>', '＞')
        if s in ('{', '}', '(', ')', '[', ']', 'while', 'for', ',', ';', '=', 'class', 'def'):
            # 省略不必要的终结符，缩减树的规模
            return ''
        return f'[{s}]'


class NilType(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __repr__(self):
        return 'NIL'

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with cls._instance_lock:
                if not hasattr(cls, "_instance"):
                    NilType._instance = object.__new__(cls)
        return NilType._instance


NIL = NilType()  # 空值（初始化但未赋值的变量）
__all__ = ['ID', 'Variable', 'NIL', 'NonTerminal', 'Number', 'String', 'Terminal']
