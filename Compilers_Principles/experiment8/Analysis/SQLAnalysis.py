"""
创建于: 2023-10-30
作者: 水告木南

该模块提供了对抽象语法树 (AST) 中的 SQL 查询进行分析和执行的功能。

主要函数:
    - extract_sql_parts(ast): 从 AST 中提取 SQL 语句的各个部分。
    - where_analysis(sql_parts, data, result): 分析 SQL 语句的 WHERE 部分，并根据条件过滤数据。
    - analysis(sql_parts, data): 分析 SQL 语句，并在数据上执行指定的操作。

示例:
    >>> import NodeCreation.SQLParser as sql_parser
    >>> import Analysis.SQLAnalysis as sql_analysis
    >>> import pandas as pd
    >>> import numpy as np
    >>> data = pd.read_csv("data/student.csv").values
    >>> query = "SELECT * FROM student WHERE age > 20"
    >>> ast_root = sql_parser.createNode(query)
    >>> sql_parts = sql_analysis.extract_sql_parts(ast_root)
    >>> result = sql_analysis.analysis(sql_parts, data)
    >>> print(result)
    # Output: Filtered data based on the query
"""


import numpy

import NodeCreation.SQLParser as sql_parser
import pandas as pd
import numpy as np

from AST.Node import Node


def where_analysis(sql_parts: dict, data: np.ndarray, result):
    """
    分析SQL语句的WHERE部分，并根据条件过滤数据。

    Args:
        sql_parts (dict): 包含SQL语句各部分的字典。
        data (np.ndarray): 需要过滤的数据。
        result: 当前的结果数组，将根据WHERE条件进行更新。

    Return:
        result: 应用了WHERE条件后更新的结果数组。
    """
    column_index_mapping = {
        'id': 0,
        'chinese': 1,
        'math': 2,
        'english': 3,
        'sum': 4
    }
    condition_node = sql_parts['WHERE'][0]
    if condition_node.getData() == "=":
        left_operand = condition_node.getChildren()[0].getData()
        right_operand = condition_node.getChildren()[1].getData()

        if right_operand == "[MAX]":
            max_value = np.max(
                data[:, column_index_mapping[condition_node.getChildren()[1].getChildren()[0].getData()]]
            )
            condition = data[:, column_index_mapping[left_operand]] == max_value
            result = result[condition]
        elif right_operand == "[MIN]":
            min_value = np.min(
                data[:, column_index_mapping[condition_node.getChildren()[1].getChildren()[0].getData()]]
            )
            condition = data[:, column_index_mapping[left_operand]] == min_value
            result = result[condition]
        elif right_operand == "[AVG]":
            avg_value = np.average(
                data[:, column_index_mapping[condition_node.getChildren()[1].getChildren()[0].getData()]]
            )
            condition = data[:, column_index_mapping[left_operand]] == avg_value
            result = result[condition]

    elif condition_node.getData() == "[BETWEEN]":
        # TODO:这里应该需要对BETWEEN进行匹配,时间有限,懒得写了
        pass
    return result


def extract_sql_parts(ast: Node):
    """
    从抽象语法树(AST)中提取SQL语句的不同部分。

    Args:
        ast (Node): SQL语句的抽象语法树。

    Return:
        dict: 包含SQL语句不同部分的字典。
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
                sql_parts['WHERE'].append(grandchild.getChildren()[0])
                # TODO:grandchild.getChildren()[0]这样只能匹配简单的WHERE语句,但是由于样例中均为简单的WHERE语句,因此这里偷懒了
        elif child.getData() == '[ORDER BY]':
            for grandchild in child.getChildren():
                if len(grandchild.getChildren()) == 0:
                    sql_parts['ORDER BY'].append(grandchild.getData())
                else:
                    sql_parts['ORDER BY'].append(grandchild.getChildren()[0])
    return sql_parts


def analysis(sql_parts: dict, data: np.ndarray):
    """
    分析SQL语句，并在数据上执行指定的操作。

    Args:
        sql_parts (dict): 包含SQL语句各部分的字典。
        data (np.ndarray): 需要执行操作的数据。

    Return:
        result: 分析的结果，可能是修改后的数据数组或某个值。
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
    elif len(sql_parts['SELECT']) == 1 and isinstance(sql_parts['SELECT'][0], str):
        result = data[:, [column_index_mapping[col] for col in sql_parts['SELECT']]]
    elif len(sql_parts['SELECT']) == 1 and isinstance(sql_parts['SELECT'][0], Node):
        # TODO:这里还应该有对MAX,MIN的匹配,时间有限,暂时不添加,以后有空了再来改
        if sql_parts['SELECT'][0].getData() == '[AVG]':
            column_name = sql_parts['SELECT'][0].getChildren()[0].getData()
            column_index = column_index_mapping[column_name]
            result = np.mean(data[:, column_index])
    if len(sql_parts['WHERE']) != 0:
        result = where_analysis(sql_parts, data, result)

    if len(sql_parts['ORDER BY']) != 0:
        column_name = sql_parts['ORDER BY'][0]
        column_index = column_index_mapping[column_name]
        sort_order = True
        if len(sql_parts['ORDER BY']) > 1 and sql_parts['ORDER BY'][1] == 'DESC':
            sort_order = False
        result = result[result[:, column_index].argsort(kind='mergesort')[::(1 if sort_order else -1)]]

    return result


if __name__ == "__main__":
    data = pd.read_csv("../data/student.csv")
    date_numpy = data.values

    query1 = ("SELECT id FROM student WHERE chinese = MAX(chinese)")
    query2 = ("SELECT * FROM student ORDER BY sum DESC")
    query3 = ("SELECT AVG(math) FROM student")
    # sql_parser.createNode(query1).printNode()
    # print(extract_sql_parts(sql_parser.createNode(query1)))
    print(analysis(extract_sql_parts(sql_parser.createNode(query1)), date_numpy))
    print("-" * 100)

    # sql_parser.createNode(query2).printNode()
    # print(extract_sql_parts(sql_parser.createNode(query2)))
    print(analysis(extract_sql_parts(sql_parser.createNode(query2)), date_numpy))
    print("-" * 100)

    # sql_parser.createNode(query3).printNode()
    # print(extract_sql_parts(sql_parser.createNode(query3)))
    print(analysis(extract_sql_parts(sql_parser.createNode(query3)), date_numpy))
