# SQL Analysis Project

该项目包括一个简单的SQL解析器和分析器，它能解析简单的SQL查询语句，并执行基本的分析操作。

## 结构

项目结构如下：

```plaintext
|-- AST/
|   |-- Node.py
|-- NodeCreation/
|   |-- SQLParser.py
|-- Analysis/
|   |-- SQLAnalysis.py
|-- tests/
|   |-- test_Node.py
|   |-- test_SQLParser.py
|   |-- test_SQLAnalysis.py
|-- run.py
|-- README.md
|-- requirements.txt
```

## 依赖项

要运行此项目，需要安装以下依赖项：

```plaintext
pytest~=7.4.3
numpy~=1.26.1
pandas~=2.1.2
ply~=3.11
```

你可以通过运行以下命令来安装这些依赖项：

```bash
pip install -r requirements.txt
```

## 使用方法

首先，你需要在`run.py`文件中指定你想要分析的SQL查询。然后，你可以通过运行`run.py`来执行分析：

```bash
python run.py
```

这将输出分析结果。

## 模块说明

### `AST/Node.py`

该模块定义了一个表示树结构节点的`Node`类。

#### 类和方法:

- `class Node`:
  - `__init__(self, data)`: 初始化Node类的实例。
    - 参数: `data`: 节点的数据。
    - 返回值: 无
  - `getData(self)`: 获取节点的数据。
    - 参数: 无
    - 返回值: 当前节点的数据。
  - `getChildren(self)`: 获取节点的子节点列表。
    - 参数: 无
    - 返回值: 子节点列表。
  - `add(self, node)`: 向子节点列表中添加一个新节点。
    - 参数: `node (Node)`: 要添加的子节点。
    - 返回值: 无
  - `printNode(self, prefix=0)`: 打印节点及其所有子节点的数据。
    - 参数: `prefix (int)`: 打印当前节点数据时的缩进级别。
    - 返回值: 无

### `NodeCreation/SQLParser.py`

该模块包含了解析SQL查询语句并创建抽象语法树（AST）的函数和类。

#### 主要函数:

- `createNode(query) -> Node`: 创建一个AST，用来表示SQL语句。
  - 参数: `query`: 输入SQL语句。
  - 返回值: 返回一个AST的根节点。

### `Analysis/SQLAnalysis.py`

该模块包含了分析SQL查询和执行分析操作的函数。

#### 主要函数:

- `where_analysis(sql_parts: dict, data: np.ndarray, result)`: 分析SQL语句的WHERE部分，并根据条件过滤数据。
  - 参数:
    - `sql_parts (dict)`: 包含SQL语句各部分的字典。
    - `data (np.ndarray)`: 需要过滤的数据。
    - `result`: 当前的结果数组，将根据WHERE条件进行更新。
  - 返回值: 应用了WHERE条件后更新的结果数组。

- `extract_sql_parts(ast: Node)`: 从抽象语法树(AST)中提取SQL语句的不同部分。
  - 参数: `ast (Node)`: SQL语句的抽象语法树。
  - 返回值: 包含SQL语句不同部分的字典。

- `analysis(sql_parts: dict, data: np.ndarray)`: 分析SQL语句，并在数据上执行指定的操作。
  - 参数:
    - `sql_parts (dict)`: 包含SQL语句各部分的字典。
    - `data (np.ndarray)`: 需要执行操作的数据。
  - 返回值: 分析的结果，可能是修改后的数据数组或某个值。

## 测试

项目包括了一些基本的单元测试，你可以通过运行以下命令来执行这些测试：

```bash
pytest tests/
```

这将运行`tests/`目录下的所有测试文件，并输出结果。

## 作者

水告木南

创建日期：2023.10.30
