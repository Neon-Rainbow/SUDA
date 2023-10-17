H = float(input('输入高度H\t'))
N = int(input('输入落地次数N\t'))
height = [H]
if N == 1:
    a = 0
else:
    for i in range(2, N + 2):
        H /= 2
        height.append(H)
        height.append(H)
print(f'共经过了{sum(height[:-2])}米\n第{N}次反弹的高度为{height[-1]}')