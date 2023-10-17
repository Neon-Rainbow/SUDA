# 编写一个程序，提示用户输入三角形的三个顶点(x1，y1)、（x2，y2）、（x3， y3），然后
# 计算三角形面积，这里假定输入的三个点能构成三角形。将面积输 出到屏幕，要求输
# 出 占 7 列，保留 2 位小数，左对齐。 三角形面积公式如下：
# s=(side1+side2+side3)/2,area=√(s(s-side1)(s-side2)(s-side3))
# 其中：side1,side2,side3 表示三角形三条边的长度
import math

x1,y1 = map(int,input('请输入第一个顶点的坐标').split(','))
x2,y2 = map(int,input('请输入第二个顶点的坐标').split(','))
x3,y3 = map(int,input('请输入第三个顶点的坐标').split(','))
side1 = math.sqrt((x1-x2)**2+(y1-y2)**2)
side2 = math.sqrt((x1-x3)**2+(y1-y3)**2)
side3 = math.sqrt((x3-x2)**2+(y3-y2)**2)
s = (side1+side2+side3)/2
area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
print(f'{area:<7.2f}')