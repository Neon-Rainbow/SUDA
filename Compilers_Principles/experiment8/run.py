"""
该模块是项目的执行脚本，负责加载数据、执行SQL查询分析，并打印分析结果。
"""

import pandas as pd
import numpy as np
from NodeCreation.SQLParser import createNode
from Analysis.SQLAnalysis import extract_sql_parts, analysis


def main():
    # 1. 加载数据
    data = pd.read_csv("./data/student.csv")
    data_numpy = data.values

    # 2. 定义查询语句
    queries = [
        "SELECT id FROM student WHERE chinese = MAX(chinese)",
        "SELECT * FROM student ORDER BY sum DESC",
        "SELECT AVG(math) FROM student"
    ]

    # 3. 执行查询并打印结果
    for i, query in enumerate(queries, 1):
        print(f"Query {i}: {query}\n")
        ast = createNode(query)
        sql_parts = extract_sql_parts(ast)
        result = analysis(sql_parts, data_numpy)
        print(result)
        print("-" * 100)


if __name__ == "__main__":
    main()
