"""
该模块定义了用于构建抽象语法树（AST）的各种节点类型。

主要包含的类有：
- _node：所有节点的基类，提供基本的节点数据结构。
- NonTerminal：非终结符节点，用于表示具有特定类型和可选值的非终结符。
- Variable：左值节点，表示引用的变量，包含类型和标识符。
- Number：数字节点，直接包含一个数字值。
- ID：标识符节点，包含标识符的名称和值。
- Terminal：终结符节点，用于表示除标识符外的其他终结符，包含其文本内容。

这些节点类型在解析Python代码并构建其AST时发挥核心作用。
"""

import re
import threading
from typing import *


class _node:
    """
    所有节点的基类。

    Attributes:
        _data (Any): 节点存储的数据。
        _children (List['_node']): 节点的子节点列表。
        _value (Any): 节点的值。
    """

    def __init__(self, data: Any):
        self._data = data
        self._children: List['_node'] = []
        self._value: Any = NIL

    @property
    def value(self) -> Any:
        """
        Returns:
            节点的值
        """
        return self._value

    @value.setter
    def value(self, value: Any) -> None:
        """
        Args:
            value (Any): 节点的值
        Returns:
            None
        """
        self._value = value

    def child(self, i: int) -> '_node':
        """获取指定索引的子节点。

        Args:
            i (int): 子节点的索引。

        Returns:
            _node: 指定索引的子节点。

        Raises:
            AssertionError: 如果索引超出范围。
        """
        return self._children[i]

    @property
    def children(self) -> List['_node']:
        """
        子节点列表
        """
        return self._children

    def add(self, node: '_node'):
        """添加子节点。

        Args:
            node (_node): 要添加的子节点。
        """
        self._children.append(node)


class NonTerminal(_node):
    """
    非终结符节点，提供type表示非终结符的类型，value（可选）为值
    """

    @property
    def type(self) -> Any:
        """
        Returns:
            非终结符的类型
        """
        return self._data

    def __str__(self) -> str:
        """
        Returns:
            str: 非终结符的字符串表示
        """
        if len(self.children) == 0:
            children = ''
        else:
            children = ' ' + ' '.join(map(str, self.children))
        r = f"[{self.type}{children}]"
        return re.sub(r'\s+', ' ', r)


class Variable(NonTerminal):
    """
    左值节点，提供type表示非终结符的类型，id表示引用的变量
    Attributes:
        _data (Any): 节点存储的数据。
        _id (Optional[str]): 引用的变量标识符。
        _children (List['_node']): 节点的子节点列表。
        _value (Any): 节点的值。
    """

    def __init__(self, data: Any) -> None:
        """
        Args:
            data (Any): 节点存储的数据。
        Returns:
            None
        """
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
    def id(self) -> Optional[str]:
        """
        变量表示符
        """
        return self._id

    @property
    def value(self):
        raise ValueError('Variable 的 value 属性不被允许使用，请通过检索符号表实现')

    @id.setter
    def id(self, i: str) -> None:
        """
        Args:
            i (str): 变量表示符
        Returns:
            None
        """
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
    Attributes:
        _data (Any): 节点存储的数据。
    """

    def __init__(self, data: Any) -> None:
        """
        Args:
            data (Any): 节点存储的数据。
        Returns:
            None
        """
        super(String, self).__init__(data)
        self._data = 'string'
        self._value = str(data[1:-1])

    def __str__(self):
        return f'String("{self._value}")'


class ID(_node):
    """
    标识符节点，提供id表示标识符名称，value为值

    Attributes:
        _data (Any): 节点存储的数据。
    """

    @property
    def id(self) -> str:
        """
        标识符名称
        Returns:
            str: 标识符名称
        """
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

    Attributes:
        _data (Any): 节点存储的数据。
    """

    @property
    def text(self) -> Any:
        """
        终结符的文本内容
        """
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
