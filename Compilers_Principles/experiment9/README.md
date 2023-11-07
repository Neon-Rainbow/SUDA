# Latex 到 PDF 转换器

本项目提供了一个将 `Latex` 内容转换成 `PDF` 文件的工具。该工具基于 `fpdf` 库实现，支持 `Latex` 的大部分语法。该项目通过将Latex文件转换为HTML字符串，再将HTML字符串转换为PDF文件的方式实现。
## 结构

项目结构如下：

```plaintext
|--AST/
|   |-- Node.py         # 该模块定义了一个用于表示树结构节点的类 Node
|
|-- AST2PDF/
|   |-- AST2HTML.py     # 该模块用于将 LaTeX 文件转换为 HTML 字符串
|   |-- HTML2PDF.py     # 该模块用于将 HTML 字符串转换为 PDF 文件
|
|--LatexParser/
|   |-- LatexParser.py  # 该模块用于将 LaTeX 文件解析为抽象语法树
|
|-- data/
|   |-- example1.tex    # 示例 LaTeX 文件
|   |-- example2.tex    # 示例 LaTeX 文件
|
|-- output/
|   |-- example1.html   # 输出的 HTML 文件
|   |-- example1.pdf    # 输出的 PDF 文件
|   |-- example2.html   # 输出的 HTML 文件
|   |-- example2.pdf    # 输出的 PDF 文件
|
|-- docs/
|   |--第9次课.docx      # 实验要求
|
|-- run.py              # 顶级脚本，用于运行项目
|-- README.md           # readme文件，项目概述和使用说明
|-- requirements.txt    # 项目依赖项说明
```


## 依赖项

要运行此项目，需要安装以下依赖项：

```plaintext
ply~=3.11
pytest~=7.4.3
fpdf2~=2.7.6
```

您可以通过运行以下命令来安装这些依赖项：

```bash
pip install -r requirements.txt
```

## 使用方法

### 方式1
使用命令行参数指定要转换的文件路径，例如：

```bash
python run.py data/example1.tex output/example1.pdf output/example1.html
```
这条指令会读取`data/example1.tex`文件，并将其转换为`output/example1.pdf`和`output/example1.html`文件。

只要是形如
```bash
python run.py {读取的latex文件位置} {输出的pdf文件位置} {输出的html文件位置}
```
的指令均可以运行
其中html文件作为中间文件，可以不指定路径.这样就不会生成html文件,而是直接将latex文件转换为pdf文件

### 方式2
也可以直接打开run.py,然后修改run.py的这一部分:
```python
if __name__ == "__main__":
    tex_filename = ""
    pdf_output_filename = ""
    html_output_filename = ""
```
修改这一部分也可以实现转换功能

## 模块说明

### `AST/Node.py`

该模块定义了一个表示树结构节点的`Node`类。

#### 类和方法

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

### `LatexParser/LatexParser.py`

该模块实现了将Latex文件解析为抽象语法树的功能。

该模块中定义的Grammar如下：

```plaintext
Grammar

Rule 0     S' -> doc
Rule 1     doc -> BEGIN LB DOC RB content END LB DOC RB
Rule 2     sectiontext -> TEXT
Rule 3     sectiontext -> TEXT BEGIN LB ITEMIZE RB item_list END LB ITEMIZE RB TEXT
Rule 4     sectiontext -> BEGIN LB ITEMIZE RB item_list END LB ITEMIZE RB TEXT
Rule 5     sectiontext -> TEXT BEGIN LB ITEMIZE RB item_list END LB ITEMIZE RB
Rule 6     content -> title abs sections
Rule 7     content -> title author abs sections
Rule 8     title -> TITLE LB TEXT RB
Rule 9     author -> AUTHOR LB TEXT RB
Rule 10    abs -> BEGIN LB ABS RB TEXT END LB ABS RB
Rule 11    sections -> sections section
Rule 12    sections -> section
Rule 13    section -> SECTION LB TEXT RB sectiontext
Rule 14    section -> SUBSECTION LB TEXT RB sectiontext
Rule 15    itemize -> BEGIN LB ITEMIZE RB item_list END LB ITEMIZE RB
Rule 16    item_list -> item_list item
Rule 17    item_list -> item
Rule 18    item -> ITEM TEXT
```
#### 类和方法
+ `def createNode(tex_file: str) -> Node:`
  创建一个抽象语法树，用来表示Latex文件。
  + 参数
    + tex_file (str): Latex文件路径。
  + 返回值
    + Node: 生成的抽象语法树的根节点。

### AST2PDF/AST2HTML.py

该模块实现了将 LaTeX 文件转换为 HTML 字符串。

#### 主要函数:

+ `Latex2Html(latex_file: str, isPrint=False) -> str`: 读取 LaTeX 文件并转换为 HTML 字符串。
  + 参数:
    + `latex_file (str)`: LaTeX 文件路径。
    + `isPrint (bool)`: 是否打印转换过程中的信息。
  + 返回值: 转换后的 HTML 字符串。

### `AST2HTML/AST2Html.py`

该模块包含了将 LaTeX 文件转换为 HTML 字符串的函数。

#### 主要函数:

+ `def Latex2Html(tex_file_name: str, html_output_filename: str = "") -> str:`读取tex_file_name中的Latex内容,将其转换为其对应的HTML格式,同时根据参数来决定是否将HTML
输出到html_output_filename中
  + 参数
    + tex_file_name (str): Latex文件路径。
    + html_output_filename (str): 输出的HTML文件路径。
  + 返回值
    + str: 转换后的HTML字符串。
+ `def Node2Html(node: Node) -> str:`
    将Node对象转换为HTML格式的字符串。
    + 参数
        + node: Node对象。用来表示Latex文档的AST
    + 返回值
        + HTML格式的字符串。
    
    

### `AST2PDF/HTML2PDF.py`

该模块包含了将 HTML 字符串转换为 PDF 文件的函数。

#### 主要函数:

+ `def Converter(tex_filename: str, pdf_output_filename: str, html_output_filename: str = "") -> None:`将tex文件转换为pdf文件
    + 参数
        + tex_filename: tex文件的路径
        + pdf_output_filename: 输出的pdf文件的路径
        + html_output_filename: 输出的html文件的路径
    + 返回值
        + None

## 作者

水告木南

创建日期：2023.11.06
