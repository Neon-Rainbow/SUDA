x1, y1 = eval(input('1坐标'))
x2, y2 = eval(input('2坐标'))
x3, y3 = eval(input('3坐标'))
l1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
l2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
l3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
c = l1 + l2 + l3
l = (l1 + l2 + l3) / 2
s = (l * (l - l1) * (l - l2) * (l - l3))
if s <= 0:
    print('无法构成三角形')
else:
    print(f'三角形周长是{c}\n三角形面积是{s}')
