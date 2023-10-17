x1, y1 = eval(input('1坐标'))
x2, y2 = eval(input('2坐标'))
x3, y3 = eval(input('3坐标'))
l1 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
l2 = ((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5
l3 = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
l = (l1 + l2 + l3) / 2
if (l * (l - l1) * (l - l2) * (l - l3))<0:
    print('无法构成三角形')
elif l1**2 + l2**2 == l3 **2 or l1**2 + l3**2 == l2 **2 or l2**2 + l3**2 == l1 **2:
    print('三角形为直角三角形')
elif l1 == l2 == l3:
    print('三角形为等边三角形')
else:
    print('普通三角形')