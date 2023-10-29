import pandas as pd


def get_max_chinese_score_student_exam_num(data):
    """
    查询语文成绩最高的学生的考号。

    参数:
        data (pd.DataFrame): 包含学生数据的pandas DataFrame。

    返回:
        int: 语文成绩最高的学生的考号。
    """
    max_score = data['语文'].max()
    return data[data['语文'] == max_score]['考号'].values[0]


def sort_students_by_total_score(data):
    """
    根据学生的总分进行排序。

    参数:
        data (pd.DataFrame): 包含学生数据的pandas DataFrame。

    返回:
        pd.DataFrame: 根据总分降序排列的学生数据。
    """
    return data.sort_values(by='总分', ascending=False)


def calculate_avg_math_score(data):
    """
    计算数学的平均分。

    参数:
        data (pd.DataFrame): 包含学生数据的pandas DataFrame。

    返回:
        float: 数学的平均分。
    """
    return data['数学'].mean()


# 以下为示例用法
if __name__ == "__main__":
    data = pd.read_csv("student.csv")

    exam_num = get_max_chinese_score_student_exam_num(data)
    print(f"语文成绩最高的学生的考号: {exam_num}")

    sorted_data = sort_students_by_total_score(data)
    print("根据总分降序排列的学生数据:")
    print(sorted_data)

    avg_math = calculate_avg_math_score(data)
    print(f"数学的平均分: {avg_math}")
