import pytest
import pandas as pd
import numpy as np
import NodeCreation.SQLParser as sql_parser
import Analysis.SQLAnalysis as sql_analysis


def test_extract_sql_parts():
    query = "SELECT * FROM student WHERE age BETWEEN 20 AND 25"
    ast_root = sql_parser.createNode(query)
    sql_parts = sql_analysis.extract_sql_parts(ast_root)
    assert 'SELECT' in sql_parts
    assert 'FROM' in sql_parts
    assert 'WHERE' in sql_parts
