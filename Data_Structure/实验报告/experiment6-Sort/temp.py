import random

lst = [i for i in range(3000,-1,-1)]
##print(lst)
##random.shuffle(lst)
with open("D:\\Programming\\C-CPP\\Csteaching\\experiment6-Sort\\data\\negative-order\\3000.txt", "w", encoding="UTF-8") as f:
    for i in range(0, 3000):
        print(f"{lst[i]}", file=f)


