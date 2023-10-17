# 请编写一个程序，从键盘输入两个时间点，格式 hh:mm:ss（时：分：秒），计算并输出
# 两个时间点相隔的秒数。
import datetime

hh1,mm1,ss1 = map(int,input('从键盘输入第一个时间点，格式 hh:mm:ss（时：分：秒）').split(':'))
hh2,mm2,ss2 = map(int,input('从键盘输入第二个时间点，格式 hh:mm:ss（时：分：秒）').split(':'))
a = datetime.timedelta(hours=hh1,minutes=mm1,seconds=ss1)
b = datetime.timedelta(hours=hh2,minutes=mm2,seconds=ss2)
delta = a-b
print(delta.seconds)