# 逻辑归结证明项目

本项目包含两个 Python 文件，分别实现了命题逻辑和谓词逻辑的归结证明。

## 文件列表

- `propositional_resolution.py`: 实现命题逻辑的归结原理。
- `predicate_resolution.py`: 实现谓词逻辑的归结证明。

## 依赖项

- Python 3.9
- `pyprover` (仅在 `predicate_resolution.py` 中需要)

## propositional_resolution.py

### 功能
实现命题逻辑的归结原理，包括文字和子句的表示，以及单个归结和多个归结的方法。

### 类和函数

#### 1. `Literal` 类

- **接口**: `Literal(name: str, negated: bool = False)`
- **参数**:
  - `name` (str): 文字的名称。
  - `negated` (bool): 表示文字是否被否定，默认为 `False`。
- **返回值**: None
- **作用**: 表示命题逻辑中的文字。

#### 2. `Clause` 类

- **接口**: `Clause(literals: list)`
- **参数**:
  - `literals` (list): 文字列表。
- **返回值**: None
- **作用**: 表示命题逻辑中的子句。

#### 3. `resolve` 函数

- **接口**: `resolve(clause1: Clause, clause2: Clause) -> Clause`
- **参数**:
  - `clause1` (Clause): 第一个子句。
  - `clause2` (Clause): 第二个子句。
- **返回值**: 一个新的子句 (Clause) 或 None。
- **作用**: 对两个子句应用归结规则，尝试得到一个新的子句。

#### 4. `resolve_multiple` 函数

- **接口**: `resolve_multiple(*clauses: Clause) -> Clause`
- **参数**:
  - `*clauses` (Clause): 多个子句。
- **返回值**: 一个新的子句 (Clause) 或 None。
- **作用**: 对多个子句应用归结规则，尝试得到一个新的子句。

## predicate_resolution.py

### 功能
实现谓词逻辑的归结证明，通过给定的谓词、变量和公式，执行归结证明，以确定是否可以从给定的公式推导出结论公式。

### 函数

#### 1. `predicate_resolution` 函数

- **接口**: `predicate_resolution(predicates: str, variables: str, givens: list, conclusion: str) -> bool`
- **参数**:
  - `predicates` (str): 空格分隔的谓词名字符串。
  - `variables` (str): 空格分隔的变量名字符串。
  - `givens` (list): 给定的公式列表。
  - `conclusion` (str): 要证明的结论公式。
- **返回值**: `True` (如果给定的公式能够推导出结论) 或 `False`。
- **作用**: 执行给定谓词、变量和公式的归结证明。

## 示例用法

### 命题逻辑归结原理

```bash
python propositional_resolution.py
```

### 谓词逻辑归结证明

```bash
python predicate_resolution.py
```

## 作者

- 水告木南

## 创建日期

- `propositional_resolution.py`: 2023-10-17
- `predicate_resolution.py`: 2023-10-21

## 许可证

此项目采用`MulanPSL-2.0 license`许可证
