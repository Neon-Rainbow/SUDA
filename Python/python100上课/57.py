people = int(input('学生总人数 = '))
lst = [0 for i in range(people)]
grade_over_90 = 0
grade_between_60_89 = 0
grade_below_60 = 0
for i in range(people):
    lst[i] = int(input(f'第{i + 1}个学生的分数 = '))
    if lst[i] <= 0:
        break
for j in lst:
    if j < 60:
        grade_below_60 += 1
    elif 60 <= j < 90:
        grade_between_60_89 += 1
    elif 90 <= j:
        grade_over_90 += 1
print(f'优秀人数为{grade_over_90}\n通过人数为{grade_between_60_89}\n不及格人数为{grade_below_60}')
