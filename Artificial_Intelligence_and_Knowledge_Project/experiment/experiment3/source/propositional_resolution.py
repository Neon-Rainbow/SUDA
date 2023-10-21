"""
该模块实现了命题逻辑的归结原理。

包括：
- Literal类：表示命题逻辑中的文字。
- Clause类：表示命题逻辑中的子句，包括单个归结和多个归结的方法。

通过归结原理，我们可以检查一组逻辑公式是否自洽，或从一组公式中推导出新的公式。
函数的使用示例包含在模块的 `__main__` 块中

作者: 水告木南
创建日期: 2023-10-17
"""


class Literal:
    """
    表示命题逻辑中的文字.

    Attributes:
        name (str): 文字的名称.
        negated (bool): 文字是否被否定.
    """

    def __init__(self, name: str, negated: bool = False):
        """
        初始化一个Literal对象。

        Args:
            name (str): 文字的名称。
            negated (bool, optional): 表示文字是否被否定。默认为False。
        """
        self.name = name
        self.negated = negated

    def __repr__(self) -> str:
        """返回此文字的字符串表示形式."""
        return f"{'~' if self.negated else ''}{self.name}"

    def __neg__(self) -> 'Literal':
        """
        返回这个文字的否定.

        Returns:
            Literal: 这个文字的否定.
        """
        return Literal(self.name, not self.negated)


class Clause:
    """
    表示命题逻辑中的子句.

    Attributes:
        literals (set[Literal]): 子句中的文字集合.
    """

    def __init__(self, literals: list) -> None:
        self.literals = set(literals)


def resolve(clause1: Clause, clause2: Clause) -> Clause:
    """
    对两个子句应用归结规则，尝试得到一个新的子句.

    Args:
        clause1 (Clause): 第一个子句.
        clause2 (Clause): 第二个子句.

    Returns:
        Clause: 如果可以应用归结规则得到一个新的子句，则返回新的子句;否则返回None.
    """
    new_clause = None
    for l1 in clause1.literals:
        for l2 in clause2.literals:
            if l1.name == l2.name and l1.negated != l2.negated:
                new_literals = (clause1.literals | clause2.literals) - {l1, l2}
                new_clause = Clause(new_literals)
    return new_clause


def resolve_multiple(*clauses: Clause) -> Clause:
    """
    对多个子句应用归结规则，尝试得到一个新的子句.

    Args:
        *clauses (Clause): 多个子句.

    Returns:
        Clause: 如果可以应用归结规则得到一个新的子句，则返回新的子句;否则返回None.
    """
    ans_clause = clauses[0]
    clause1 = clauses[0]
    for clause2 in clauses:
        if clause1 != clause2:
            ans_clause = resolve(ans_clause, clause2)
    return ans_clause


if __name__ == "__main__":
    # 示例用法:
    c1 = Clause([Literal("P", negated=True), Literal("Q")])
    c2 = Clause([Literal("Q", negated=True), Literal("R")])
    c3 = Clause([Literal("P")])
    clauses = resolve_multiple(c1, c2, c3)
    print(clauses.literals)
