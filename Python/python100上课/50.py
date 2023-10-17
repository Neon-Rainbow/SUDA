x1 = float(input('x1 = '))
y1 = float(input('y1 = '))
r = float(input('r = '))
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))
distance = ((x1-x2)**2+(y1-y2)**2)**0.5
if distance <= r:
    print('在圆内')
else:
    print('在圆外')
