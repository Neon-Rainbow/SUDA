class Node:
    """
    表示树结构的一个节点。

    Attributes:
        _data: 节点的数据。
        _children: 子节点列表。
    """

    def __init__(self, data):
        """
        初始化Node类的实例。

        Args:
            data: 节点的数据。
        """
        self._data = data
        self._children = []

    def getData(self):
        """
        获取节点的数据。

        Returns:
            当前节点的数据。
        """
        return self._data

    def getChildren(self):
        """
        获取节点的子节点列表。

        Returns:
            子节点列表。
        """
        return self._children

    def add(self, node):
        """
        向子节点列表中添加一个新节点。

        Args:
            node (Node): 要添加的子节点。
        """
        self._children.append(node)

    def printNode(self, prefix=0):
        """
        打印节点及其所有子节点的数据。

        Args:
            prefix (int): 打印当前节点数据时的缩进级别。
        """
        data_to_print = self._data.getData() if isinstance(self._data, Node) else self._data
        print(f"{'  ' * prefix}+ {data_to_print}")
        for child in self._children:
            if isinstance(child, Node):  # 确保子节点是Node对象
                child.printNode(prefix + 1)
            else:
                print(f"{'  ' * (prefix + 1)}+ {child}")
