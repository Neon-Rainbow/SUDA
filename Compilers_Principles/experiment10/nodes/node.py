#!/usr/bin/env python
# coding=utf-8

from typing import List, Union, Optional


class Node:
    """
    表示树结构中的一个节点。

    Attributes:
        _data: 节点中存储的数据。
        _children: 子节点列表。
        _value: 与节点相关联的可选数值。
    """

    def __init__(self, data: Union[str, int, float]) -> None:
        """
        初始化 Node 类的一个新实例。

        Args:
            data: 要存储在节点中的数据。
        """
        self._data = data
        self._children: List['Node'] = []
        self._value: Optional[float] = None

    def get_data(self) -> Union[str, int, float]:
        """
        获取节点中存储的数据。

        Returns:
            节点中存储的数据。
        """
        return self._data

    def set_value(self, value: float) -> None:
        """
        为节点设置一个数值。

        Args:
            value: 要设置的数值，为浮点数。
        """
        self._value = value

    def get_value(self) -> Optional[float]:
        """
        获取节点的数值。

        Returns:
            节点的数值，如果未设置则返回 None。
        """
        return self._value

    def get_child(self, i: int) -> 'Node':
        """
        通过索引获取子节点。

        Args:
            i: 要获取的子节点的索引。

        Returns:
            指定索引处的子节点。
        """
        return self._children[i]

    def get_children(self) -> List['Node']:
        """
        获取所有子节点。

        Returns:
            子节点的列表。
        """
        return self._children

    def add(self, node: 'Node') -> None:
        """
        向此节点添加一个子节点。

        Args:
            node: 要作为子节点添加的节点。
        """
        self._children.append(node)

    def print_node(self, prefix: int) -> None:
        """
        以树状结构打印节点及其子节点。

        Args:
            prefix: 用于缩进打印节点的前缀级别。
        """
        print('  ' * prefix, '+', self._data)
        for child in self._children:
            child.print_node(prefix + 1)


def num_node(data: Union[str, int, float]) -> Node:
    """
    创建具有数值的 Node 实例。

    Args:
        data: 要存储在节点中的数据。

    Returns:
        一个具有给定数据和数值的 Node 实例。
    """
    t = Node(data)
    t.set_value(float(data))
    return t
