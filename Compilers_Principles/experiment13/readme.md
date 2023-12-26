# 基于PLY的Python解析(4)

## 项目结构图
```
基于PLY的Python解析(4)
├── python_parser
│   ├── main.py # 项目的入口文件。处理命令行参数，读取Python脚本文件
│   ├── node.py #  定义了用于构建抽象语法树（AST）的节点类
│   ├── parser.out
│   ├── parsetab.py
│   ├── py_lex.py # 定义了如何将Python代码拆分成一个个的词法单元（tokens）
│   ├── py_yacc.py # 定义了Python语言的语法规则
│   ├── stu.py # 示例Python脚本，用于测试解释器
│   └── translation.py #  负责将抽象语法树转换成可执行的代码
├── readme.md
└── requirements.txt
```

## 项目流程图
```mermaid
graph TD;
    main_py[main.py] --> py_lex_py[py_lex.py]
    main_py --> py_yacc_py[py_yacc.py]
    py_lex_py -- tokens --> py_yacc_py
    py_yacc_py -- AST --> node_py[node.py]
    node_py -- AST --> translation_py[translation.py]
    translation_py --> main_py
```

## 项目运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行

```bash
python3 main.py {需要分析的文件}
```

或运行可执行文件,例如
```bash
./dist/main/main python_parser/stu.py 
```

当需要分析的文件不存在时,程序会报错,报错内容为`不正确的用法

示例用法:
```bash
python3 python_parser/main.py python_parser/stu.py
```

输出:
```plaintext
语法树： [Program [Statements [Statements [Statements [Statements [Statement [Class ID('Student') [Functions [Functions [Functions [Function ID('__init__') [Args [Args [Args [AID('self')] ID('name')] ID('age')] ID('score')] [Statements [Statements [Statements [Statement [Assignment [Variable ID('self') [.] ID('name')] [Expr [Term [Factor [Variable ID('name')]]]]]]] [Statement [Assignment [Variable ID('self') [.] ID('age')] [Expr [Term [Factor [Variable ID('age')]]]]]]] [Statement [Assignment [Variable ID('self') [.] ID('score')] [Expr [Term [Factor [Variable ID('score')]]]]]]] ]] [Function ID('add_score') [Args [Args ID('self')] ID('score')] [Statements [Statement [Assignment [Variable ID('self') [.] ID('score')] [Expr [Expr [Term [Factor [Variable ID('self') [.] ID('score')]]]] [+] [Term [Factor [Variable ID('score')]]]]]]] ]] [Function ID('print_info') [Args ID('self')] [Statements [Statement [Print [print] [Exprs [Exprs [Expr [Term [Factor [Variable ID('self') [.] ID('name')]]]]] [Expr [Term [Factor [Variable ID('self') [.] ID('age')]]]]] ]]] ]] ]]] [Statement [Assignment [Variable ID('a')] [Expr [Term [Factor [Call ID('Student') [Exprs [Exprs [Exprs [Expr [String String("xiaoming")]]] [Expr [Term [Factor Number(12)]]]] [Expr [Term [Factor Number(20)]]]] ]]]]]]] [Statement [Expr [Term [Factor [Call ID('a') [.] ID('add_score') [Exprs [Expr [Term [Factor Number(60)]]]] ]]]]]] [Statement [Expr [Term [Factor [Call ID('a') [.] ID('print_info') ]]]]]]]
运行结果：
xiaoming 12
当前变量表： {'Student': <Class object 'Student'>, 'a': <PyObject Student at 0x1030c9e50>}
```

### translate函数的工作流程

```mermaid
graph TD;
    A[开始] -->|检查break或return标志| B[返回return_value]
    B --> C{是否为NonTerminal节点}
    C -->|否| Z[结束]
    C -->|是| D{节点类型}
    D -->|Function| E[处理Function节点]
    E --> F[创建和存储Function]
    F --> Z
    D -->|Class| G[处理Class节点]
    G --> H[创建和存储Class]
    H --> Z
    D -->|If| I[处理If节点]
    I --> J[根据条件执行相应语句]
    J --> Z
    D -->|Else| K[处理Else节点]
    K --> L[执行else或elif语句]
    L --> Z
    D -->|While| M[处理While节点]
    M --> N[循环执行While语句]
    N --> Z
    D -->|For| O[处理For节点]
    O --> P[循环执行For语句]
    P --> Z
    D -->|Break| Q[设置break标志]
    Q --> Z
    D -->|Return| R[处理Return节点]
    R --> S[设置return值和标志]
    S --> Z
    D -->|其他类型| T[递归处理子节点]
    T --> U[执行翻译操作]
    U --> Z
```