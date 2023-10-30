import pytest
from create_node.sql_parser import createNode


def test_createNode():
    query1 = ('SELECT COUNT(column1) AS count_col1 '
              'FROM table1 AS tab1 '
              'WHERE column1 BETWEEN value1 AND value2 '
              'ORDER BY count_col1 DESC '
              )
    print(createNode(query1).printNode())
