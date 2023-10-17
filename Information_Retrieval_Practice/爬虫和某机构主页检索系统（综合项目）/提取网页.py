import requests
import re
from bs4 import BeautifulSoup
import ssl
import urllib3
import urllib.request

# 网页正文提取模块
urllib3.disable_warnings()
ssl._create_default_https_context = ssl._create_unverified_context

encoding = "UTF-8"
page = "http://scst.suda.edu.cn/"  # 该网址为需要爬取的总网页，可进行修改
web_list = [page]  # 该列表用于存放网站
web_queue = [page]  # 该队列用于存放网站


def fun1(web, mode=0):  # mode用于指定函数返回值，该函数用于提取网页正文
    response = requests.get(web, verify=False, timeout=30)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    # 正文提取 模式0
    # web_body = soup.get_text()
    # 标题提取 模式1
    # web_title = soup.title.string
    # 链接提取 模式2
    # links = soup.find_all('a')
    # link_lst = []
    # for item in links:
    #     link_lst.append(item.get("href"))
    if mode == 0:
        web_body = soup.get_text()
        return web_body
    elif mode == 1:
        web_title = soup.title.string
        return web_title
    elif mode == 2:
        links = soup.find_all('a')
        link_lst = []
        for item in links:
            link_lst.append(item.get("href"))
        return link_lst


def fun2(web_list_, web_queue_, link_list):
    for i in link_list:
        if re.search("\.suda\.edu\.cn", str(i)):
            if i not in web_list_:
                web_queue_.append(i)
                web_list_.append(i)


def print_to_txt(web, file_path):
    file_name = change_module(web)
    with open(f"{file_path}\\{file_name}.txt", "w", encoding="utf-8") as f:
        print("title:", file=f)
        print(fun1(web, 1), file=f)
        print("body:", file=f)
        print(fun1(web, 0), file=f)


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_name, file_content):
    with open("text\\web" + file_name.replace('/', '_') + ".html", "wb") as f:
        f.write(file_content)


def fun3(url, file_name):
    html = getHtml(url)
    saveHtml(file_name, html)


def queue_pop(queue):  # 对队列进行处理，弹出队列的第一项
    return queue.pop(0)


def change_module(web):  # 去掉网站中的http://,\等无法保存的特殊字符
    temp1 = re.sub(r"/", "", web)
    temp2 = re.sub(r"http:", "", temp1)
    temp3 = re.sub(r"\\", "", temp2)
    temp4 = re.sub("\?", "", temp3)
    return temp4


count = 0
while len(web_queue) > 0 and len(web_list) < 1000:
    if count > len(web_list):
        break
    else:
        print(f"第{count + 1}个网站:")
        temp = web_list[count]
        print(f"正在处理:\n{temp}")
        fun3(temp, f"file{count + 1}")
        count += 1
        print(web_list)
        # temp = queue_pop(web_queue)
        # print(temp)
        # print("Label1")
        link_temp_list = fun1(temp, 2)
        if len(link_temp_list) == 0:
            continue

        # print(link_temp_list)
        # print("Label2")
        fun2(web_list, web_queue, link_temp_list)
        # print("Label3")
        print_to_txt(temp, "text\\txt")
        # print("Label4")
        # print(web_list)
        print(len(web_list))
        print("-" * 30)
