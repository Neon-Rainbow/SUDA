# 实验8

## 1 
> basename、dirname、paste命令的熟练掌握。自己设计场景，实现basename、 dirname、paste的使用，要求每条命令使用3次。
> 

```bash
#!/bin/bash

# 创建命令列表
commands=(
    "basename /usr/bin/sort"
    "basename /var/log/syslog.log .log"
    "basename /home/user/document.txt"
    "dirname /usr/bin/sort"
    "dirname /var/log/syslog.log"
    "dirname /home/user/document.txt"
    "paste file1.txt file2.txt # 合并两个文件的内容（横向连接）"
    "paste -s file1.txt # 将一个文件的内容转换为单列"
    "paste -d ',' file1.txt file2.txt # 使用不同的分隔符合并文件内容"
)

# 遍历命令列表并执行
for cmd in "${commands[@]}"
do
    echo "Running: $cmd"
    eval $cmd
    echo
done

```

## 2

>   ACL知识点的熟练掌握，自己设计场景，要求实现:
>
>   +   为xx用户(自己额外创建的用户)赋予读写xx文件(自己创建的文件)的权限，并验证。
>   +   为xx用户(自己额外创建的用户)赋予读写xx目录(自己创建的目录)的权限，并验证。

```bash
#!/bin/bash

# 定义用户名、文件名和目录名
username="newuser"
filename="myfile.txt"
dirname="mydir"

echo "正在创建新用户: $username"
sudo useradd $username

echo "正在创建新文件: $filename，并为 $username 用户赋予读写权限"
touch $filename
setfacl -m u:$username:rw $filename

echo "正在创建新目录: $dirname，并为 $username 用户赋予读写权限"
mkdir $dirname
setfacl -m u:$username:rw $dirname

echo "输出 $filename 的 ACL 设置:"
getfacl $filename

echo "输出 $dirname 的 ACL 设置:"
getfacl $dirname

# 删除操作
echo "正在删除用户: $username"
sudo userdel $username

echo "脚本执行完成。"

```

## 3

>   在Linux环境下，自己创建一个C++程序(要求:包含多个文件)，并进行运行(可执行文件)。

项目结构图:

```
hello_world_program/
|
|--	main.cpp
|--	hello.h
|--	hello.cpp
```

三个文件内容如下:

```c++
// hello.h
#ifndef HELLO_H
#define HELLO_H

void hello_world(); // 函数声明

#endif

```

```C++
// hello.cpp
#include <iostream>
#include <chrono>
#include <format>
#include "hello.h"

void hello_world() {
    std::cout << "hello world" << std::endl;
    auto now = std::chrono::system_clock::now();

    // 转换为time_t对象
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);

    // 转换为可读的形式
    std::cout << std::format("Current Time:{}", std::ctime(&now_time)) << std::endl;
}


```

```c++
// main.cpp
#include "hello.h"

int main() {
    hello_world();
    return 0;
}

```

运行:
不使用cmake:

```bash
g++ -std=c++20 main.cpp hello.cpp -o hello_world_program # 使用C++20标准编译

./hello_world_program
```

使用cmake:

CMakeLists.txt内容:

```cmake
cmake_minimum_required(VERSION 3.10)
project(HelloWorldProject)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 包含头文件
include_directories(${PROJECT_SOURCE_DIR})

# 指定生成目标
add_executable(HelloWorld main.cpp hello.cpp)

```

项目结构图

```
hello_world_program/
|
|--	main.cpp
|--	hello.h
|--	hello.cpp
|--	CMakeLists.txt
```

编译过程

```bash
cmake .
make
./HelloWorld

```

## 4

[教程](https://help.aliyun.com/zh/ecs/use-cases/build-a-lamp-stack-on-ubuntu-instances)



