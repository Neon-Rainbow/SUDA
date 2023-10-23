"""
test_parser.py: 包含对 main 模块中 atom_count 函数的测试用例。

此模块定义了一个测试用例类 TestParser，该类包含了对 atom_count 函数的多个单元测试。
每个测试方法对应一个特定的测试场景，确保 atom_count 函数在各种输入条件下都能正确工作。

Usage:
    python -m unittest discover tests  # 从项目根目录运行所有测试
"""

import unittest
from src.main import atom_count


class TestParser(unittest.TestCase):
    """
    测试用例类，对 main 模块中的 atom_count 函数进行测试.
    测试样例均来自实验要求
    """

    def test_single_element(self):
        self.assertEqual(atom_count("He"), 1)

    def test_element_and_quantity(self):
        self.assertEqual(atom_count("H2"), 2)

    def test_complex_molecule(self):
        self.assertEqual(atom_count("H2SO4"), 7)

    def test_organic_molecule(self):
        self.assertEqual(atom_count("CH3COOH"), 8)

    def test_salt(self):
        self.assertEqual(atom_count("NaCl"), 2)

    def test_large_molecule(self):
        self.assertEqual(atom_count("C60H60"), 120)


if __name__ == '__main__':
    unittest.main()
