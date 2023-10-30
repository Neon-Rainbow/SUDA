import pytest
from AST.Node import Node

def test_node_creation():
    node = Node("root")
    assert node.getData() == "root"
    assert node.getChildren() == []

def test_node_add_children():
    node = Node("root")
    child_node = Node("child")
    node.add(child_node)
    assert node.getChildren() == [child_node]

# ... 更多测试 ...
