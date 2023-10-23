# Chemical Formula Parser

本项目是一个化学分子式解析器，能够解析给定的化学分子式，并计算其中的原子总数。项目使用Python编程语言，并利用Python Lex-Yacc（PLY）库实现词法分析和语法分析。

## 项目结构

```plaintext
编译原理实验7 ChemicalFormulaParser/
├── src/
│   ├── lexer.py      # 词法分析器模块
│   ├── parser.py     # 语法分析器模块
│   └── main.py        # 主执行模块，包含atom_count函数
├── tests/
│   └── test_parser.py # 测试代码,用来测试给出的样例
├── docs/
│	├── 实验要求.pdf     # 本次编译原理实验的实验要求
│	├── 实验7实验报告.pdf # 本次编译原理实验的实验报告的pdf格式
│	└── 实验7实验报告.docx # 本次编译原理实验的实验报告docx格式
├── run.py            # 顶级脚本，用于运行项目
└── readme.md。       # readme文件,用来项目概述和使用说明
```

## 文件与模块

### src/

#### lexer.py

此模块包含词法分析器，用于识别化学分子式中的符号和数字。

接口：
- `lexer`: 词法分析器实例，用于分析化学分子式字符串。

#### parser.py

此模块包含语法分析器，用于解析化学分子式，并计算原子数量。

接口：
- `parser`: 语法分析器实例，用于解析由词法分析器提供的令牌。

#### main.py

此模块包含主执行函数和化学分子式解析器的测试代码。

接口：
- `atom_count(formula: str) -> int`: 计算给定化学分子式中的原子数量。

### tests/

#### test_parser.py

此模块包含对`src/main.py`中`atom_count`函数的测试用例。

测试方法：
- `test_molecule`: 测试有机分子的情况。

    


## 安装依赖

项目python版本:

+   Python 3.9.6 (default, Aug 11 2023, 19:44:49) 
+   [Clang 15.0.0 (clang-1500.0.40.1)] on darwin

在运行项目之前，需要安装`ply`库和`pytest`库。可以通过以下命令来安装：

```bash
pip3 install ply
pip3 install pytest
```

## 运行项目

1. 运行`run.py`文件来测试项目：
```bash
python run.py
```

## 使用方法

在`src/main.py`中，`atom_count`函数是项目的主要接口。你可以通过调用此函数并传递化学分子式来获取元素的数量。

```python
from src.main import atom_count

# 示例
result = atom_count("H2SO4")
print(result)  # 输出: 7
```

## 测试

可以通过运行`tests/test_parser.py`文件来执行测试，或者使用以下命令从项目的根目录运行所有测试：

```bash
 python3 -m pytest
```

