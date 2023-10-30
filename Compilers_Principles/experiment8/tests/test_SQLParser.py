import pytest
from NodeCreation.SQLParser import createNode

def test_create_node():
    query = ("SELECT * FROM student WHERE age BETWEEN 20 AND 25")
    ast_root = createNode(query)
    assert ast_root.getData() == "QUERY"

