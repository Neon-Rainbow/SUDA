"""
该模块包含一个用于执行谓词逻辑归结证明的函数。

该模块定义了 `predicate_resolution` 函数，该函数接受一组谓词、变量、给定的公式和一个结论公式，
然后执行归结证明以确定是否可以从给定的公式推导出结论公式。

函数的使用示例包含在模块的 `__main__` 块中，显示了如何调用 `predicate_resolution` 函数并输出归结证明的结果。

该模块依赖于 `pyprover` 库来执行归结证明。

作者: 水告木南
创建日期: 2023-10-21
"""


from pyprover import props, terms, FA, TE, proves


def predicate_resolution(predicates, variables, givens, conclusion):
    """
    执行给定谓词、变量和公式的归结证明。

    该函数接受一组谓词、变量和公式，执行归结证明，然后返回证明的结果。

    Args:
        predicates (str): 空格分隔的谓词名字符串。
        variables (str): 空格分隔的变量名字符串。
        givens (list): 给定的公式列表。
        conclusion (str): 要证明的结论公式。

    Returns:
        bool: 如果给定的公式能够推导出结论，则返回 True；否则返回 False。
    """
    # 创建谓词和变量字典
    predicate_dict = {name: prop for name, prop in zip(predicates.split(), props(predicates))}
    variable_dict = {name: var for name, var in zip(variables.split(), terms(variables))}

    # 解析给定的公式和结论
    def parse_formula(formula):
        for name, prop in predicate_dict.items():
            formula = formula.replace(name, f"predicate_dict['{name}']")
        for name, var in variable_dict.items():
            formula = formula.replace(name, f"variable_dict['{name}']")
        return eval(formula)

    givens_parsed = [parse_formula(formula) for formula in givens]
    conclusion_parsed = parse_formula(conclusion)

    # 执行归结证明
    result = proves(givens_parsed, conclusion_parsed)

    return result


if __name__ == "__main__":
    predicates = "R S"
    variables = "x y z"
    givens = ["FA(x, R(x) >> S(x))", "TE(y, R(y))"]
    conclusion = "TE(z, S(z))"
    result = predicate_resolution(predicates, variables, givens, conclusion)
    print(f"The conclusion {conclusion} is {'valid' if result else 'invalid'}.")
