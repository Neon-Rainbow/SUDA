def Bubble_sort1(lst): # 从小到大
    length = len(lst)
    for i in range(length):
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


def Bubble_sort2(lst): # 从大到小
    length = len(lst)
    for i in range(length):
        for j in range(length - i - 1):
            if lst[j] < lst[j + 1]:
                lst[j + 1], lst[j] = lst[j], lst[j + 1]
    return lst


lst = [0 for i in range(10)]
for i in range(10):
    lst[i] = int(input(f"lst[{i}] = "))
print(f"升序排序后为{Bubble_sort1(lst)}")
print(f"降序排序后为{Bubble_sort2(lst)}")
