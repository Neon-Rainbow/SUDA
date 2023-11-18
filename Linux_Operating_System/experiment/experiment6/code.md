## 1. 工具grep的实验报告

### **命令要求**：

> 涉及到书本上P154-155共7个命令 + 2个额外命令(课外查找)。

```shell
# 书本上的命令
grep -c 'pattern' filename # 计算文件filename中包含字符串pattern的行数
grep -i 'pattern' filename # 搜索文件filename中包含pattern的行，不区分大小写
grep -n 'pattern' filename # 显示文件filename中每一个包含pattern的行及其行号
grep -v 'pattern' filename # 显示文件filename中所有不包含pattern的行
grep -A 2 'pattern' filename # 显示文件filename中每一个包含pattern的行，以及紧随其后的两行
grep -B 2 'pattern' filename # 显示文件filename中每一个包含pattern的行，以及其前面的两行
grep -C 2 'pattern' filename # 显示文件filename中每一个包含pattern的行，以及其前后各两行的内容
# 课外查找的额外命令
grep -E 'end$' filename # 使用扩展正则表达式匹配任何以'end'结尾的行
grep -V # 显示版本信息
```

### **功能要求**：
> 涉及到书本上P155-158(也就是11.1.1-11.1.8所有的功能) + 2个额外功能(课外查找)，每个功能要体现3次(不能与书上例子一样)。
```shell
grep -n "std" 1.cc # 过滤出带有某个关键词的行，并输出行号
grep -nv "std" 1.cc # 过滤出不带有某个关键词的行，并输出行号
grep [0-9] 1.cc # 过滤出所有带数字的行
grep -v [0-9] 1.cc # 过滤出所有不带数字的行
grep -v '^#' 1.cc # 过滤掉所有以#开头的行
grep -v "^#" 1.cc | grep -v "^$" # 过滤掉所有空行和以#开头的行
grep "s.d" 1.cc # 过滤出任意一个字符和重复字符
grep "(std)*" 1.cc # 过滤出含有零个或多个std
egrep ":+" 1.cc # 过滤出一个或多个:
egrep ":?" 1.cc # 过滤出零或一个:
grep -v [0-9] *1* # 查找文件名中包含 1 的文件中不包含数字的行
```

```shell
cat >> script.sh << "EOF"
#!/bin/bash

# 过滤出带有某个关键词的行，并输出行号
echo "Command: grep -n \"std\" 1.cc # 过滤出带有某个关键词的行，并输出行号"
grep -n "std" 1.cc

# 过滤出不带有某个关键词的行，并输出行号
echo "Command: grep -nv \"std\" 1.cc # 过滤出不带有某个关键词的行，并输出行号"
grep -nv "std" 1.cc

# 过滤出所有带数字的行
echo "Command: grep [0-9] 1.cc # 过滤出所有带数字的行"
grep [0-9] 1.cc

# 过滤出所有不带数字的行
echo "Command: grep -v [0-9] 1.cc # 过滤出所有不带数字的行"
grep -v [0-9] 1.cc

# 过滤掉所有以#开头的行
echo "Command: grep -v '^#' 1.cc # 过滤掉所有以#开头的行"
grep -v '^#' 1.cc

# 过滤掉所有空行和以#开头的行
echo "Command: grep -v \"^#\" 1.cc | grep -v \"^$\" # 过滤掉所有空行和以#开头的行"
grep -v "^#" 1.cc | grep -v "^$"

# 过滤出任意一个字符和重复字符
echo "Command: grep \"s.d\" 1.cc # 过滤出任意一个字符和重复字符"
grep "s.d" 1.cc

# 过滤出含有零个或多个std
echo "Command: grep \"(std)*\" 1.cc # 过滤出含有零个或多个std"
grep "(std)*" 1.cc

# 过滤出一个或多个:
echo "Command: egrep \":+\" 1.cc # 过滤出一个或多个:"
egrep ":+" 1.cc

# 过滤出零或一个:
echo "Command: egrep \":?\" 1.cc # 过滤出零或一个:"
egrep ":?" 1.cc

# 查找文件名中包含 1 的文件中不包含数字的行
echo "Command: grep -v [0-9] *1* # 查找文件名中包含 1 的文件中不包含数字的行"
grep -v [0-9] *1*
EOF

chmod +x script.sh
./script.sh
```

### **区别阐述**：
> 阐述grep和egrep的联系与区别，并列举3个例子，示例这种区别(不能与书上例子一样)。
`grep` 和 `egrep` 都是 Linux 中用于在文件中搜索特定模式的命令。它们的主要区别在于它们处理正则表达式的方式。

- `grep`：`grep` 命令使用基本正则表达式进行搜索。在基本正则表达式中，一些元字符（如 `+`、`?`、`|` 等）需要使用反斜杠 (`\`) 进行转义才能发挥其特殊功能。

- `egrep`：`egrep` 是 `grep -E` 的快捷方式，它使用扩展正则表达式进行搜索。在扩展正则表达式中，元字符无需转义即可发挥其特殊功能。

下面是一些例子来说明这种区别：

1. **使用 `grep` 搜索以 'a' 或 'b' 结尾的行**：
    ```shell
    grep 'a\\|b$' filename
    ```
   这将返回文件中以 'a' 或 'b' 结尾的所有行。

2. **使用 `egrep` 执行相同的搜索**：
    ```shell
    egrep 'a|b$' filename
    ```
   这将返回与 `grep` 相同的结果，但是我们不需要使用反斜杠转义 `|` 字符。

3. **使用 `grep` 搜索包含字符串 'a|b' 的行**：
    ```shell
    grep 'a|b' filename
    ```
   这将返回文件中包含字符串 'a|b' 的所有行。

## 2. 工具sed的初步掌握

### **要求**：
> 涉及到书本上P160-163(也就是11.2.1-11.2.6所有的功能)，每个功能要体现3次(不能与书上例子一样)。

将指令输入到sed_script.sh中

```shell
cat >> sed_script.sh << "EOF"
echo "打印某行，这里分别打印第2、第3和第4行"
sed -n '2p' 1.cc
sed -n '3p' 1.cc
sed -n '4p' 1.cc

echo "打印包含某个字符串的行，这里分别打印包含"root"、"user"和"bin"的行"
sed -n '/root/p' 1.cc
sed -n '/user/p' 1.cc
sed -n '/bin/p' 1.cc

echo "删除某些行，这里分别删除第5、第6和第7行"
sed '5d' 1.cc
sed '6d' 1.cc
sed '7d' 1.cc

echo "替换字符或字符串，这里分别将"root"替换为"user"，"bin"替换为"dev"，以及"/bin/bash"替换为"/usr/bin/zsh""
sed 's/root/user/' 1.cc
sed 's/bin/dev/' 1.cc
sed 's/\/bin\/bash/\/usr\/bin\/zsh/' 1.cc

echo "调换两个字符串的位置，这里分别调换"x:0:0:root"与"root:x:0:0"、"usr:bin"与"bin:usr"、"dev:sbin"与"sbin:dev"的位置"
sed 's/\(x:0:0:\)root/root:\1/' 1.cc
sed 's/\(usr:\)bin/bin:\1/' 1.cc
sed 's/\(dev:\)sbin/sbin:\1/' 1.cc

echo "直接修改文件的内容，这里分别将文件中的"root"替换为"user"，"bin"替换为"dev"，以及"/bin/bash"替换为"/usr/bin/zsh""
sed -i 's/root/user/' 1.cc
sed -i 's/bin/dev/' 1.cc
sed -i 's/\/bin\/bash/\/usr\/bin\/zsh/' 1.cc
EOF
```

给sed_script.sh运行权限

```shell
chmod +x sed_script.sh
```

运行该脚本
```shell
./sed_script.sh
```

## 3. 工具sed的深度掌握

### **要求**：
> 探索书本之外的3个额外功能，每个功能要体现3次。

```shell
cat >> sed_extra_script.sh << "EOF"
echo "插入文本到特定行后"
sed '1a New Line 1' ./passwd
sed '2a New Line 2' ./passwd
sed '3a New Line 3' ./passwd

echo "在特定行前添加文本"
sed '1i Header 1' ./passwd
sed '2i Header 2' ./passwd
sed '3i Header 3' ./passwd

echo "选择性地打印模式空间内容"
sed -n '/^start/p' ./passwd
sed -n '/end$/p' ./passwd
sed -n '/^start/!;/end$/!p' ./passwd
EOF
```

## 4. 工具awk的实验报告

### **要求**：
> 11.3.1-11.3.3的功能都要涉及到，每个功能要体现3次。
```shell
cat  >> awk_script.sh << "EOF"
#!/bin/bash

# 截取文档中的某个段
echo "截取前三行"
awk 'NR>=1 && NR<=3' ./passwd

echo "截取用户名为 'daemon' 和 'bin' 之间的行"
awk '/daemon/,/bin/' ./passwd

echo "截取用户名字段"
awk -F':' '{print $1}' ./passwd

# 匹配字符或字符串
echo "匹配含有 'nologin' 的行"
awk '/nologin/' ./passwd

echo "匹配 UID 为 100 的用户"
awk -F':' '$3==100' ./passwd

echo "匹配含有 'nologin' 并打印用户名和shell"
awk -F':' '/nologin/ {print $1, $NF}' ./passwd

# 条件操作符
echo "打印 UID 小于 10 的用户"
awk -F':' '$3<10 {print $1}' ./passwd

echo "打印 UID 大于 100 且使用 '/bin/bash' 的用户"
awk -F':' '$3>100 && $NF=="/bin/bash" {print $1}' ./passwd

echo "打印 GID 在 100 至 200 范围内的用户"
awk -F':' '$4>=100 && $4<=200 {print $1}' ./passwd
EOF
```

## 5. grep\egrep\sed\awk\vim的介绍和区别

> 结合书上内容与课外资料进行介绍和比较。

`grep`、`egrep`、`sed`、`awk`和`vim`都是在Linux中用于处理文本的强大工具，每个工具都有其特定的用途和功能。

- `grep`：`grep`是一个用于在文件或输入流中查找匹配正则表达式的行并将这些匹配行打印到标准输出的工具。它是最简单的工具，主要用于简单的文本匹配和打印。

- `egrep`：`egrep`是`grep`的扩展版本，它提供了与`grep -E`相同的输出，但工作速度更快⁵。它可以处理文本并执行比较和算术运算。

- `sed`：`sed`可以查找和修改数据，但其语法比`grep`稍微复杂一些。它是一个流编辑器，可以对输入流（文件或管道输入）进行转换。

- `awk`：`awk`是一种完整的编程语言，可以处理文本并执行比较和算术运算。它是一个用于处理文本的脚本语言，提供了许多`grep`和`sed`中不存在的功能。

- `vim`：`vim`是一个文本编辑器，它是Vi编辑器的增强版本，通常在命令行界面中使用，但也有可用于标准桌面使用的GUI版本。


## 6. grep\egrep\sed\awk\vim涉及到的特殊字符的总结和比较

`grep`、`egrep`、`sed`、`awk`和`vim`都是在Linux中用于处理文本的强大工具，每个工具都有其特定的用途和功能。以下是这些工具中涉及到的一些特殊字符的总结和比较：

- `grep`：`grep`是一个用于在文件或输入流中查找匹配正则表达式的行并将这些匹配行打印到标准输出的工具。它是最简单的工具，主要用于简单的文本匹配和打印。在`grep`中，有一些特殊字符需要转义，例如`$`、`*`、`|`、`^`、`(`、`)`和`]`。

- `egrep`：`egrep`是`grep`的扩展版本，它提供了与`grep -E`相同的输出，但工作速度更快²⁶。它可以处理文本并执行比较和算术运算²³。在`egrep`中，也有一些特殊字符需要转义，例如`$`、`*`、`|`、`^`、`(`、`)`和`]`。

- `sed`：`sed`可以查找和修改数据，但其语法比`grep`稍微复杂一些²³。它是一个流编辑器，可以对输入流（文件或管道输入）进行转换。在`sed`中，有一些特殊字符需要转义，例如`$`、`*`、`|`、`^`、`(`、`)`和`]`[^10^]。

- `awk`：`awk`是一种完整的编程语言，可以处理文本并执行比较和算术运算。它是一个用于处理文本的脚本语言，提供了许多`grep`和`sed`中不存在的功能。在`awk`中，有一些特殊字符需要转义，例如`$`、`*`、`|`、`^`、`(`、`)`和`]`。

- `vim`：`vim`是一个文本编辑器，它是Vi编辑器的增强版本，通常在命令行界面中使用，但也有可用于标准桌面使用的GUI版本。在`vim`中，有一些特殊字符需要转义，例如`$`、`*`、`|`、`^`、`(`、`)`和`]`[^20^]。


## 7. 命令解释与实践验证

- `$ awk -F: '{print $1,$5}' file.txt`
- `$ awk -F'[:\t]' '{print $1,$3}' file.txt`
- `$ awk -F: '{print $1,$5}' file.txt`
- `$ awk '{print $3}' file.txt`
- `$ awk '/^(no|so)/' file.txt`
- `$ awk '/^[ns]/{print $1}' file.txt`
- `$ awk '$1 ~/[0-9][0-9]$/(print $1}' file.txt`
- `$ awk '$1 == 100 || $2 < 50' file.txt`
- `$ awk '/test/{print $1 + 10}' file.txt`
- `$ awk '$1 ~/test/{count = $2 + $3; print count}' file.txt`
- `$ awk -F: '{IGNORECASE=1; $1 == "MARY"{print NR,$1,$2,$NF}' file.txt`
- `$ awk {name[x++]=$2};END{for(i=0;i<NR;i++) print i,name[i]}' file.txt`
- `$ awk '{count[$1]++} END{for(name in count) print name,count[name]}' file.txt`
- `$ awk '{line[x++]=$1} END{for(x in line) delete(line[x])}' file.txt`

```shell
# 打印以':'分隔的第一个和第五个字段
$ awk -F: '{print $1,$5}' file.txt

# 打印以':'或制表符分隔的第一个和第三个字段
$ awk -F'[:\t]' '{print $1,$3}' file.txt

# 打印以':'分隔的第一个和第五个字段
$ awk -F: '{print $1,$5}' file.txt

# 打印每行的第三个字段
$ awk '{print $3}' file.txt

# 打印以'no'或'so'开头的行
$ awk '/^(no|so)/' file.txt

# 打印以'n'或's'开头的行的第一个字段
$ awk '/^[ns]/{print $1}' file.txt

# 如果第一个字段以两位数字结尾，则打印第一个字段
$ awk '$1 ~ /[0-9][0-9]$/ {print $1}' file.txt

# 打印第一个字段等于100或第二个字段小于50的行
$ awk '$1 == 100 || $2 < 50' file.txt

# 对于包含'test'的行，打印第一个字段加10
$ awk '/test/{print $1 + 10}' file.txt

# 如果第一个字段包含'test'，则打印第二个字段和第三个字段的和
$ awk '$1 ~/test/ {count = $2 + $3; print count}' file.txt

# 对于第一个字段为"MARY"（不区分大小写）的行，打印行号、第一个字段、第二个字段和最后一个字段
$ awk -F: '{IGNORECASE=1; $1 == "MARY" {print NR,$1,$2,$NF}}' file.txt

# 将第二个字段存储在数组'name'中，并在结束时打印它们
$ awk '{name[x++]=$2} ; END {for(i=0; i<NR; i++) print i,name[i]}' file.txt

# 统计第一个字段的出现次数，并在结束时打印名称和计数
$ awk '{count[$1]++} END {for(name in count) print name,count[name]}' file.txt

# 在结束时删除存储第一个字段的'line'数组的元素
$ awk '{line[x++]=$1} END {for(x in line) delete(line[x])}' file.txt

```
执行这些指令:

```shell
cat >> awk_script.sh << "EOF"
#!/bin/bash

# 打印并执行 AWK 命令
echo "\$ awk -F: '{print \$1,\$5}' file.txt"
awk -F: '{print $1,$5}' file.txt

echo "\$ awk -F'[:\t]' '{print \$1,\$3}' file.txt"
awk -F'[:\t]' '{print $1,$3}' file.txt

echo "\$ awk '{print \$3}' file.txt"
awk '{print $3}' file.txt

echo "\$ awk '/^(no|so)/' file.txt"
awk '/^(no|so)/' file.txt

echo "\$ awk '/^[ns]/{print \$1}' file.txt"
awk '/^[ns]/{print $1}' file.txt

echo "\$ awk '\$1 ~/[0-9][0-9]$/(print \$1}' file.txt"
awk '$1 ~/[0-9][0-9]$/(print $1}' file.txt

echo "\$ awk '\$1 == 100 || \$2 < 50' file.txt"
awk '$1 == 100 || $2 < 50' file.txt

echo "\$ awk '/test/{print \$1 + 10}' file.txt"
awk '/test/{print $1 + 10}' file.txt

echo "\$ awk '\$1 ~/test/{count = \$2 + \$3; print count}' file.txt"
awk '$1 ~/test/{count = $2 + $3; print count}' file.txt

echo "\$ awk -F: '{IGNORECASE=1; \$1 == \"MARY\"{print NR,\$1,\$2,\$NF}' file.txt"
awk -F: '{IGNORECASE=1; $1 == "MARY"{print NR,$1,$2,$NF}' file.txt

echo "\$ awk '{name[x++]=\$2};END{for(i=0;i<NR;i++) print i,name[i]}' file.txt"
awk '{name[x++]=$2};END{for(i=0;i<NR;i++) print i,name[i]}' file.txt

echo "\$ awk '{count[\$1]++} END{for(name in count) print name,count[name]}' file.txt"
awk '{count[$1]++} END{for(name in count) print name,count[name]}' file.txt

echo "\$ awk '{line[x++]=\$1} END{for(x in line) delete(line[x])}' file.txt"
awk '{line[x++]=$1} END{for(x in line) delete(line[x])}' file.txt

EOF

chmod +x awk_script.sh

./awk_script.sh
```

向file.txt中输入内容

```bash
cat >> file.txt << "EOF"
std::vector<int> v;
# 这是一个注释行
nobody expects the Spanish Inquisition
so it begins
12345
line with 99 at the end99
100, first field is 100
42, this field is less than 50
This line contains the word test
A test line with numbers: 10, 20
s.d sequence in this line
stdstd repeated sequence
one colon: here
two colons:: here
line with numbers 1, 2, 3
line without numbers
EOF
```




## 8. 命令cd\mkdir\rm\cp\mv\cat\chmod的复习

### **概述**：
> 结合书上内容，概况阐述总结每个命令。

这些命令都是在Unix或类Unix系统（比如Linux和macOS）中常用的命令行工具，用于进行文件和目录的管理。下面是每个命令的英文名称和它们的基本功能：

1. `cd` (Change Directory): 用于更改当前工作目录。例如 `cd /home` 会将当前目录切换到 `/home`。

2. `mkdir` (Make Directory): 用于创建新的目录。例如 `mkdir new_folder` 会在当前目录下创建一个名为 `new_folder` 的新目录。

3. `rm` (Remove): 用于删除文件或目录。例如 `rm file.txt` 会删除名为 `file.txt` 的文件。如果配合 `-r` 标志（递归），它也可以删除目录及其包含的所有文件。

4. `cp` (Copy): 用于复制文件或目录。例如 `cp source.txt destination.txt` 会将 `source.txt` 文件复制到 `destination.txt`。

5. `mv` (Move): 用于移动或重命名文件或目录。例如 `mv old_name.txt new_name.txt` 会将 `old_name.txt` 重命名为 `new_name.txt`。

6. `cat` (Concatenate): 通常用于查看、创建和合并文件。例如 `cat file.txt` 会在终端显示 `file.txt` 文件的内容。

7. `chmod` (Change Mode): 用于改变文件或目录的权限。例如 `chmod 755 file.txt` 会将 `file.txt` 的权限设置为所有者可读写执行、组和其他用户可读执行。

### **实践操作**：
> 实践操作每个命令2次。

```shell
cd .
cd ~

mkdir Directory
mkdir -p project/src

rm 1.txt
rm -r test/

cp 1.txt 2.txt
cp -r folder1 folder2

mv file1.txt file2.txt
mv folder1 folder2

cat file.txt
cat file1.txt file2.txt > combined.txt

chmod 644 file.txt
chmod +x script.sh

```
