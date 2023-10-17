import re
import jieba
import os
import numpy.lib.npyio
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings

warnings.filterwarnings("ignore")
numpy.set_printoptions(threshold=1000000)

# seg_list = jieba.lcut("我来到北京清华大学")
# string = " ".join(seg_list)
# print(string)
# print(seg_list)
# tf_idf = TfidfVectorizer().fit_transform(seg_list)
# print(tf_idf)
# 分词分局模块，倒排索引模块和网页排序模块
file_path = "text\\txt"
file_list = os.listdir(file_path)
title_list = []
corpus = []
text_all = ""
for each_file in file_list:
    with open(f"{file_path}\\{each_file}", "r", encoding="UTF-8") as f:
        text_temp = f.read()
        title_temp = re.findall("title:\n(.+?)\nbody:", text_temp, re.S)[0]
        list_temp = jieba.lcut(text_temp)
        fenci_temp = " ".join(list_temp)
        title_list.append(title_temp)
        f.close()
    corpus.append(fenci_temp)

tf_idf = TfidfVectorizer()
tfidf_matrix = tf_idf.fit_transform(corpus)

# print(tf_idf.vocabulary_)
# print(tfidf_matrix[0:2][1:1])
# print("-" * 30)
word = tf_idf.get_feature_names()
# print(word)
weight = tfidf_matrix.toarray()
# print(weight)
for i in range(len(weight)):  # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
    # print(f"下面是第{i}个文档的tf-idf值，文档名为{file_list[i]}")
    with open(f"text\\tfidf值\\{file_list[i]}的TF_IDF值.txt", "w", encoding="utf-8") as f:
        for j in range(len(word)):
            # print(word[j], weight[i][j])
            print(word[j], weight[i][j], file=f)

# 查询模块
queue_sentence = input("请输入需要查询的句子(输出后请按下Enter键):")


def search_word(queue_word):
    sort_tfidf = {}
    count = 0
    for each_word_count in range(len(word)):
        if str(word[each_word_count]) == str(queue_word):
            count = each_word_count
            break
    else:
        count = -1
    if count == -1:
        print("查询的词语在文档中没有出现或为停止词，请检查是否有输入错误")
    else:
        for i in range(len(weight)):
            if weight[i][count] != 0:
                sort_tfidf[i] = weight[i][count]
        sorted_tfidf = sorted(sort_tfidf.items(), key=lambda x: x[1], reverse=False)
        title_queue = sorted_tfidf[0][0]

        file_name = file_list[title_queue]
        with open(f"text\\txt\\{file_name}", "r", encoding="utf-8") as f:
            all_of_text = f.read()
            all_of_text_after_change = re.sub(f"{queue_word}", f"##{queue_word}##", all_of_text)

            print(all_of_text_after_change)
        with open(f"text\\查询结果\\'{queue_word}'的查询结果.txt", "w", encoding="utf-8") as g:
            print(f"最符合'{queue_word}'这一搜索词的文章的title为{title_list[title_queue]}，文档序号为{title_queue}", file=g)
            print("该文档内容为(查询词已被着重标记):", file=g)
            print(all_of_text_after_change, file=g)
        print(r"本次搜索结果已被保存至目录text/查询结果")


def search_sentence(sentence):
    search_word_list = jieba.lcut(sentence)
    for i in range(len(search_word_list)):
        print(f"输入的句子中的第{i + 1}个单词为{search_word_list[i]},句子中共有{len(search_word_list)}个单词")
        search_word(search_word_list[i])
        print("-" * 30)


search_sentence(queue_sentence)
