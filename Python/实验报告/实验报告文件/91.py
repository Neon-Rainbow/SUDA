def fib(i):
    if i == 1 or i == 2:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)


i = int(input('输入斐波那契数列的项数'))
print(f'第{i}项为{fib(i)}')
