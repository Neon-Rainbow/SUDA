# Linux实验7

## 1
> 查阅资料，根据自己的理解，回答什么是shell脚本。

Shell脚本是一种用于自动化执行命令的脚本语言，通常用于Linux或Unix操作系统。它是一系列命令的集合，可以通过Shell程序解释和执行。

## 2
> shell脚本有几种运行方式，它们的区别是什么?

Shell脚本主要有两种运行方式：

1.  作为可执行程序：将脚本文件设置为可执行权限（使用`chmod +x`命令），然后直接运行。
2.  通过Shell解释器直接调用：使用命令如`sh script.sh`或`bash script.sh`来执行。

两者的区别主要在于是否需要明确指定使用哪个Shell解释器。

## 3
> 如何使脚本可执行?

使用`chmod +x script.sh`命令给予脚本文件执行权限。

## 4

> 在shell脚本中，如何写入注释?写注释的目的是什么?

注释使用`#`符号开始，例如：

```shell
# 这是一个注释。
```
注释的目的是解释代码的功能或目的，以便于阅读和维护。
## 5
> shell脚本的预设变量:
> 怎么向脚本传入第1个参数、第2个参数
> 如何获得脚本名、脚本所有参数、脚本参数个数

+   向脚本传入参数：使用`$1`来表示第一个参数，`$2`表示第二个参数。
+   获得脚本名：使用`$0`。
+   获得所有参数：使用`$@`或`$*`。
+   获得参数个数：使用`$#`。

## 6

> 如何让shell脚本得到来自终端的输入?用例子验证。

```shell
echo "请输入一个值："
read value
echo "您输入的值是：$value"
```



## 7

> 编写shell脚本，实现:输入两个字符串，输出这两个字符串的连接起来的字
> 符串(需实现4种形式连接，见例子)。 如输入字符串hello和字符串linux，输出
> (1) hellolinux
> (2)  hello linux
> (3)  hello: linux
> (4)  hello LINUX

```shell
#!/bin/bash
echo "请输入两个字符串："
read str1 str2
echo "(1) $str1$str2"
echo "(2) $str1 $str2"
echo "(3) $str1: $str2"
echo "(4) $str1 ${str2^^}"

```



## 8
> 两个整数相加，有4种实现方法，分别是什么，用例子验证。

1.  使用`expr`命令：`sum=$(expr $a + $b)`
2.  使用双括号：`sum=$((a + b))`
3.  使用`let`命令：`let sum=a+b`
4.  使用`bc`命令：`sum=$(echo "$a + $b" | bc)`

## 9
> 编写shell脚本，实现:检查某一目录下是否存在某个文件，存在与否都要输出相应提示信息。

```shell
#!/bin/bash
echo "请输入文件名："
read filename
if [ -f "$filename" ]; then
    echo "文件存在"
else
    echo "文件不存在"
fi

```



## 10
> 脚本的第一行#! /bin/bash表示什么意思?

这是一个Shebang行，指定脚本应当使用哪个解释器来执行，这里指定的是Bash。

## 11

> [ $a == $b ] 和 [ \$a -eq\$b ] 有什么区别?

`[ $a == $b ]`用于字符串比较，而`[ $a -eq $b ]`用于整数比较。

## 12
> = 和 == 有什么区别?

在Shell脚本中，`=` 用于赋值，`==` 用于字符串比较。

## 13
> 课本p187的12.7的shell脚本练习题，添加代码注释，运行验证。

1.   编写shell脚本，计算1~100的和。
2.   编写shell脚本，输入一个数字n并计算1 ~n的和。要求:如果输人的数字小于1，则重新输入， 直到输人正确的数字为止。
3.   编写shell脚本 ，把/root/目录下的所有目录(只需要一级)复制到/imp/目录下。
4.   编写shell脚本，批量建立用户user _00、user _O1.. user_99。要求:所有用户同属于users组。 
5.   编写shell脚本，截取文件test. log中包含关键词abc的行中的第1列(假设分隔符为:)，然后把截 取的数字排序(假设第1列为数字)，最后打印出重复超过10次的列。
6.   编 写 s h e l l 脚 本 ，判 断 输 人的 I P 是 否 正 确 。要 求 :I P 的 规 则 是 n 1 . n 2 . n 3 . n 4 ，其 中 1 < n 1 < 2 5 5 , 0 < n 2 < 2 5 5 ， 0<n3<255, 0<n4<255 ).

```shell
#!/bin/bash
# 计算1到100的和

sum=0
for i in {1..100}; do
    sum=$((sum + i))
done

echo "The sum of numbers from 1 to 100 is: $sum"

```

```shell
#!/bin/bash
# 计算1到n的和，n是用户输入的数字

sum=0
while true; do
    read -p "Enter a number (>=1): " n
    if [[ $n -ge 1 ]]; then
        for i in $(seq 1 $n); do
            sum=$((sum + i))
        done
        echo "The sum of numbers from 1 to $n is: $sum"
        break
    else
        echo "Please enter a number greater than or equal to 1."
    fi
done

```

```shell
#!/bin/bash
# 复制/root/目录下的所有一级目录到/imp/目录

mkdir -p /imp
for dir in /root/*/; do
    cp -r "$dir" /imp/
done

```

```shell
#!/bin/bash
# 批量创建用户user_00到user_99，并加入users组

for i in $(seq -w 0 99); do
    useradd -m "user_$i"
    usermod -aG users "user_$i"
done

```

```shell
#!/bin/bash
# 截取包含关键词abc的行的第1列并排序，打印重复超过10次的列

awk -F ':' '/abc/ {print $1}' test.log | sort | uniq -c | awk '$1 > 10 {print $2}'

```

```shell
#!/bin/bash
# 判断输入的IP是否正确

read -p "Enter an IP address: " ip

if [[ $ip =~ ^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$ ]]; then
    echo "The IP address $ip is valid."
else
    echo "The IP address $ip is not valid."
fi

```



## 14
> 编写一个shell脚本，实现两个变量之间的加减乘除以及求余运算。实现哪种 运算(加、减、乘、除、求余)，取决于用户的输入。运行验证。

```shell
#!/bin/bash
echo "请输入两个数字："
read a b
echo "选择运算：加(1) 减(2) 乘(3) 除(4) 求余(5)"
read op
case $op in
    1) result=$((a + b)) ;;
    2) result=$((a - b)) ;;
    3) result=$((a * b)) ;;
    4) result=$((a / b)) ;;
    5) result=$((a % b)) ;;
    *) echo "无效输入" && exit 1 ;;
esac
echo "结果：$result"

```



## 15
> 编写shell脚本，提示用户输入linux或python(不区分大小写),并判断用户输入的是linux还是python,或是其它信息。运行验证。

```shell
#!/bin/bash
echo "请输入'linux'或'python'（不区分大小写）："
read input
case "${input,,}" in
    linux) echo "您输入的是linux" ;;
    python) echo "您输入的是python" ;;
    *) echo "输入了其他信息" ;;
esac

```



## 16
> 编写shell脚本，计算0-50以内所有偶数之和。运行验证。

```shell
#!/bin/bash
sum=0
for (( i=0; i<=50; i+=2 ))
do
    sum=$((sum + i))
done
echo "0到50内所有偶数的和是：$sum"

```



## 17
> 编写shell脚本，首先生成10个随机数字，并输出这个10数字，同时显示其中的最大值和最小值。

```shell
#!/bin/bash
echo "10个随机数："
for i in {1..10}; do
    num=$((RANDOM % 100))
    echo $num
    nums[$i]=$num
done
min=${nums[1]}
max=${nums[1]}
for n in ${nums[@]}; do
    ((n > max)) && max=$n
    ((n < min)) && min=$n
done
echo "最大值：$max, 最小值：$min"

```




## 18
> 编写shell脚本，在一个目录下的所有文件的文件名后面加“test”。

```shell
#!/bin/bash
for file in *; do
    mv "$file" "${file}test"
done

```



## 19

> 阐述break、continue、exit在循环中的作用，并编写shell脚本验证。

+   `break`：退出循环。
+   `continue`：跳过当前循环迭代，继续下一个迭代。
+   `exit`：退出脚本。

```shell
#!/bin/bash

echo "演示break命令："
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo "循环次数：$i"
done

echo "演示continue命令："
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "循环次数：$i"
done

echo "演示exit命令："
for i in {1..5}; do
    echo "循环次数：$i"
    if [ $i -eq 3 ]; then
        echo "exit命令将终止脚本"
        exit
    fi
done

```



## 20
> 结合所学，写 3 个 shell 脚本， 并说明他们实现了什么功能。

1.   检测网站可用性脚本

```shell
#!/bin/bash

sites=("http://baidu.com" "http://google.com" "http://github.com")
for site in "${sites[@]}"
do
  status=$(curl -o /dev/null -s -w "%{http_code}\n" $site)
  if [ $status -eq 200 ]; then
    echo "网站 $site 可访问"
  else
    echo "网站 $site 不可访问, 状态码: $status"
  fi
done

```

2.   系统信息报告脚本

```shell
#!/bin/bash

echo "主机名：$(hostname)"
echo "系统运行时间：$(uptime -p)"
echo "当前用户：$(whoami)"
echo "网络配置："
ifconfig

```

3.   监控CPU和内存使用率脚本

```shell
#!/bin/bash

while true; do
    echo "--- $(date) ---"
    echo "CPU和内存使用情况:"
    uptime
    echo "内存使用情况:"
    free -h
    echo "-----------------------"
    sleep 2
done

```



## 21

> 本地主机为Linux系统，远程登录服务器Linux系统，有几种方式，分别是什么，有什么特点、优缺点?

1.  **SSH**: SSH是一种加密的网络协议，可以在不安全的网络中为远程登录提供安全的通信环境。它是Linux系统中最常用的远程登录方式之一。SSH具有安全性高、稳定性好、支持多种加密算法等优点。但是，SSH需要在服务器上安装SSH服务，且在使用时需要输入用户名和密码，不够方便。
2.  **VNC**: VNC是一种远程桌面协议，可以在不同的操作系统之间共享桌面。它可以在图形界面下远程登录Linux服务器，支持多用户同时登录，且可以在不同的操作系统之间共享桌面。但是，VNC的安全性较差，需要在服务器上安装VNC服务。
3.  **Telnet**: Telnet是一种远程登录协议，可以在不安全的网络中为远程登录提供通信环境。它是Linux系统中最早的远程登录方式之一，但是由于其安全性较差，现在已经很少使用了。

## 22
> 本地主机为windows系统，远程登录服务器Linux系统，有几种方式，分别是什么，有什么特点、优缺点?

1.  **SSH (Secure Shell) 使用客户端如PuTTY**
    +   特点：SSH是最常用的安全远程登录方法。PuTTY是一个流行的SSH和Telnet客户端，用于Windows系统。
    +   优点：提供安全的加密连接，支持命令行操作，支持文件传输（使用额外工具如WinSCP）。
    +   缺点：只提供文本界面，初次配置可能稍显复杂。
2.  **Windows Subsystem for Linux (WSL)**
    +   特点：WSL允许在Windows上运行Linux环境，可以直接使用Linux命令行工具。
    +   优点：无需额外软件即可直接在Windows中使用Linux命令行。
    +   缺点：并非完整的Linux系统，某些特定的Linux功能可能不支持。
3.  **VNC (Virtual Network Computing)**
    +   特点：提供图形界面的远程访问。
    +   优点：能够访问Linux的图形界面，适合需要图形界面操作的场景。
    +   缺点：配置相对复杂，对网络带宽要求较高，安全性低于SSH。
4.  **RDP (Remote Desktop Protocol) 通过第三方软件**
    +   特点：RDP是Windows系统中常用的远程桌面协议，可通过第三方软件在Linux上实现。
    +   优点：提供完整的桌面体验。
    +   缺点：需要在Linux服务器上安装和配置额外的软件，比如xrdp。
5.  **远程桌面管理器（如Remote Desktop Manager, mRemoteNG）**
    +   特点：这些管理器集成了多种远程桌面协议。
    +   优点：一个工具内支持多种协议，方便管理多个远程连接。
    +   缺点：配置相对复杂，有些功能可能需要付费版。