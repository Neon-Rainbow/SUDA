# 请编写一个程序，显示当前北京时间。要求显示格式如下：
# a) 当前时间是：几时：几分：几秒
# b) 输出示例：
# c) 当前时间是： 14：26：32

import time

now_time = time.localtime()
print(f'当前时间是： {now_time.tm_hour}: {now_time.tm_min}: {now_time.tm_sec}')