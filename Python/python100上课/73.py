import random

lst = [0 for i in range(7)]
for i in range(7):
    lst[i] = random.randint(1,10) #int(input(f'第{i+1}位评委的打分为 '))
lst.sort()
lst = lst[1:6]
print(f'选手得分为{sum(lst) / len(lst)}')
