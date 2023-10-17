string = 'python'
n = int(input(f'准备删除{string}的第几个字母？'))
print(f'Python删除第{n}个字母后为{string[:n - 1] + string[n:]}')
