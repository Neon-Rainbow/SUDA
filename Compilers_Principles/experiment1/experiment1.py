# 实现中缀表达式转化为后缀表达式
import string
import re
import os


# 该函数用来判断后缀转中缀时,运算符的优先级
def priority(i):
    if i in ['×', '*', '/']:
        return 2
    elif i in ['+', '-']:
        return 1


def infix_to_postfix(infix: str) -> string:
    infix_list: list = infix.split()  # 该列表用来存放中缀表达式
    operation_stack: list = []  # 该栈用于存放操作符
    output_list: list = []  # 该列表用于存放最终输出结果
    for i in infix_list:
        if i.isnumeric():
            output_list.append(i)
        elif i == '(':
            operation_stack.append(i)
        elif i == ')':
            while len(operation_stack) != 0 and operation_stack[-1] != '(':
                output_list.append(operation_stack.pop())
            operation_stack.pop()
        elif i in ['*', '/', '+', '-']:
            while operation_stack and operation_stack[-1] != '(' and priority(operation_stack[-1]) >= priority(i):
                output_list.append(operation_stack.pop())
            operation_stack.append(i)
    while operation_stack:  # 若最终操作符栈中还有操作符,则将这些操作符同意添加到最终输出结果中
        output_list.append(operation_stack.pop())
    return ' '.join(output_list)  # 返回最终输出结果


# 正则表达式练习
def validate_filename(filename: str) -> bool:
    pattern: str = r'.+\.(jpg|jpeg|gif|bmp)'  # 该正则表达式用来匹配含有.jpg,.jpeg,.gif,.bmp的字符串
    lowercase_filename: str = filename.lower()
    is_match = re.match(pattern, lowercase_filename)
    return is_match and lowercase_filename.split('.')[-1] in ['jpg', 'jpeg', 'gif',
                                                              'bmp']  # 需要判断匹配到的字符串的尾部是否是jpg,.jpeg,.gif,.bmp


def date_match(text: str) -> list:
    date_pattern: str = r'\d{1,2}/\d{1,2}/\d{1,4}'  # 匹配开头为一到两个数字,然后是/,然后是一到两个数字,然后/,结尾是四位数字的字符串
    matches = re.findall(date_pattern, text)[0]
    return matches


def phone_number_extraction(phone_number: str) -> str:
    pattern = r'\((\d+)\)'  # 提取字符串中括号内的内容
    match = re.search(pattern, phone_number)
    if match:
        return match.group(1)
    else:
        return '未找到区号'


def extract_hyperlink(filepath: str) -> list:
    with open(filepath, 'r') as f:
        text = f.read()
    hyperlink: str = r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"'  # 提取text中超链接标签中的链接
    hyperlink_list: list = re.findall(hyperlink, text)
    return hyperlink_list


def extract_text(filepath: str) -> list:
    with open(filepath, 'r', encoding='UTF-8') as f:
        text = f.read()
    title_pattern: str = r'<title>(.+)</title>'  # 提取title标签中的标题部分
    body_pattern: str = r'<p>(.*?)</p>'  # 提取正文标签中的正文
    title: str = re.findall(title_pattern, text)[0]  # 提取title
    body: list = re.findall(body_pattern, text)  # 提取body
    return [title, body]  # 返回标题和正文


if __name__ == '__main__':
    print("9 - 5 + 2的中缀表达式转后缀表达式的结果是:", end="")

    print(infix_to_postfix('9 - 5 + 2'))

    print(date_match('safsadfas30/9/2001sfsadfa'))

    print(validate_filename('0f0002JnyrTgRygqLGhM76.jpg'))

    print(phone_number_extraction('(0512)\68078800-6852)'))

    hyperlink_list = extract_hyperlink("re_example/list.html")
    print(hyperlink_list)

    file1 = open("output/link.html.txt", "w")
    for i in hyperlink_list:
        file1.write(i + "\n")
    file1.close()

    file2 = open("output/content.html.txt", 'w')
    title = extract_text("re_example/content.html")[0]
    body = extract_text("re_example/content.html")[1]
    file2.write("title:" + title + '\n')
    file2.write("body:" + "\n")
    for i in body:
        file2.write(i)
    file2.close()
