def fib(n):
    if n == 1:
        return 1
    elif n== 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    n = int(input("请输入:"))
    print(f"斐波那契数列第{n}项为{fib(n)}")