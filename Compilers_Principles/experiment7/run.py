"""
run.py: 包含执行化学分子式解析器的主入口。

此脚本为化学分子式解析器提供了一个简单的用户界面。
用户可以输入一个化学分子式，脚本将返回该分子式中的原子数量。

Usage:
    python run.py  # 从命令行运行此脚本，按提示输入化学分子式
"""

from src.main import atom_count


def main() -> None:
    """
    主函数，提示用户输入化学分子式，并输出原子数量.

    从用户获取化学分子式的输入, 调用 atom_count 函数来计算原子数量,
    然后将结果打印到控制台.

    Args:
        None

    Returns:
        None.但是会在终端上显示出输入的化学分子式中的原子数
    """
    formular = input("请输入化学分子式: ")
    print(f"{formular} 中的原子数量为 {atom_count(formular)}")


if __name__ == '__main__':
    main()
