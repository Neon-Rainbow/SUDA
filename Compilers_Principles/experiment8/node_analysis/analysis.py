import numpy

import create_node.sql_parser as sql_parser
import pandas as pd
import numpy as np

from AST.node import Node


def extract_sql_parts(ast: Node):
    """

    """
    sql_parts = {
        'SELECT': [],
        'FROM': [],
        'WHERE': [],
        'ORDER BY': []
    }

    for child in ast.getChildren():
        if child.getData() == '[SELECT]':
            for grandchild in child.getChildren()[0].getChildren():
                if isinstance(grandchild, Node):
                    sql_parts['SELECT'].append(grandchild.getChildren()[0])
                else:
                    sql_parts['SELECT'].append(grandchild)
        elif child.getData() == '[FROM]':
            for grandchild in child.getChildren()[0].getChildren():
                sql_parts['FROM'].append(grandchild.getChildren()[0].getData())
        elif child.getData() == '[WHERE]':
            for grandchild in child.getChildren():
                sql_parts['WHERE'].append(grandchild.getChildren())
        elif child.getData() == '[ORDER BY]':
            for grandchild in child.getChildren():
                if len(grandchild.getChildren()) == 0:
                    sql_parts['ORDER BY'].append(grandchild.getData())
                else:
                    sql_parts['ORDER BY'].append(grandchild.getChildren()[0])
    return sql_parts



def analysis(sql_parts: dict, data: numpy.ndarray):
    """
    对sql语句进行分析，返回结果。

    Args:
        sql_parts: sql语句的各个部分
        data: 数据
    Returns:
        return: 分析结果
    """
    column_index_mapping = {
        'id': 0,
        'chinese': 1,
        'math': 2,
        'english': 3,
        'sum': 4
    }

    result = None
    if len(sql_parts['SELECT']) == 1 and sql_parts['SELECT'][0] == '*':
        result = data
    else:
        result = data[:, [column_index_mapping[col] for col in sql_parts['SELECT']]]

    if len(sql_parts['WHERE']) != 0:
        pass

    if len(sql_parts['ORDER BY']) != 0:
        pass

    return result



if __name__ == "__main__":
    data = pd.read_csv("../data/student.csv")
    date_numpy = data.values

    query1 = ("SELECT id FROM student WHERE chinese = MAX(chinese)")
    query2 = ("SELECT * FROM student ORDER BY sum DESC")
    query3 = ("SELECT id FROM student WHERE (chinese BETWEEN value1 AND value2) AND (english BETWEEN 60 AND 80)")
    # query3 = ("SELECT AVG(math) FROM student")
    sql_parser.createNode(query1).printNode()
    print(extract_sql_parts(sql_parser.createNode(query1)))
    print(analysis(extract_sql_parts(sql_parser.createNode(query1)), date_numpy))

    sql_parser.createNode(query2).printNode()
    print(extract_sql_parts(sql_parser.createNode(query2)))
    # print(analysis(extract_sql_parts(sql_parser.createNode(query2)), date_numpy))

    sql_parser.createNode(query3).printNode()
    print(extract_sql_parts(sql_parser.createNode(query3)))
    # print(analysis(extract_sql_parts(sql_parser.createNode(query3)), date_numpy))
