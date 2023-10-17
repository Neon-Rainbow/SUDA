lst = [i for i in range(1, 100000, 2)]
with open("D:\\Programming\\C-CPP\\Csteaching\\experiment5-Search\\data\\100000.txt", "w", encoding="UTF-8") as f:
    for i in lst:
        print(f"{i}", file=f)
