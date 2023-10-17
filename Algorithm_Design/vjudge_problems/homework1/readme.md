解题思路

输入num,可以得到一个list,例如num = 10的时候,list = [1,0,1,1,1,0,1,0,1,0,1,1,1,0,1],num = (1010)

list[index] = num[i]

其中index和i的对应关系如下:
$$
\text{bin}(index)的后置1的个数为i的大小 \\
例如index = 5,\text{bin}(index) = 101,后置1的个数为1,因此i = 1 \\
index = 4,\text{bin}(index) = 100,后置1的个数为0,因此i = 0
$$

