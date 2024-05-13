#import "@preview/sourcerer:0.2.1": code
#import "@preview/mitex:0.2.2": *

#align(center, text(17pt)[
  实验八 设计一个简单的文件系统
])

#set heading(numbering: "一.  1")

= 实验目的
#block[
  #set enum(numbering: "(1)")
  + 深入理解Linux 文件系统的原理。
  + 学习并理解Linux 的VFS 文件系统管理技术。
  + 学习并理解Linux 的ext2 文件系统实现技术。
  + 设计并实现一个简单的类ext2 文件系统。
]


= 实验内容
设计并实现一个类似于ext2 但能够对磁盘上的数据块进行加密的文件系统 myext2。本实验的主要内容如下：
#block[
  #set enum(numbering: "(1)")
  + 添加一个类似于ext2 的文件系统myext2。
  + 修改myext2 文件系统的magic number。
  + 修改文件系统操作。
  + 添加文件系统创建工具。
]

对于myext2 文件系统，要求如下：
#block[
  #set enum(numbering: "(1)")
  + myext2 文件系统的物理格式定义与ext2 文件系统基本一致，但myext2 文 件系统的magic number  是0x6666，而 ext2 文件系统的magic number  是0xEF53。
  + myext2 文件系统是ext2 文件系统的定制版本，前者不但支持ext2 文件系统的部分操作，而且添加了文件系统创建工具。
]

= 实验步骤和结果

== 添加一个类似于 ext2 的文件系统 myext2
+ 在 Linux Shell 下执行如下操作：
  #code(
    ```sh
cd /usr/src/linux-4.15 
cd fs 
cp –R ext2 myext2
cd /usr/src/linux-4.15/fs/myext2 
mv ext2.h myext2.h 
cd /lib/modules/$(uname -r)/build/include/linux 
cp ext2_fs.h myext2_fs.h 
cd /lib/modules/$(uname -r)/build/include/asm-generic/bitops
cp ext2-atomic-setbit.h myext2-atomic-setbit.h
    ```
  )
+ 修改文件内容
  + 使用如下脚本将原来文件中的 EXT2 替换成 MYEXT2，ext2 替换成 myext2。

#code(
  ```C
  #include <stdio.h>
  #include <stdlib.h>
  int main() {
    printf("Hello, World!\n");
    return 0;
  }
  ```
)

#mitex(`
  \newcommand{\f}[2]{#1f(#2)}
  \f\relax{x} = \int_{-\infty}^\infty
    \f\hat\xi\,e^{2 \pi i \xi x}
    \,d\xi
`)

= 实验总结与思考