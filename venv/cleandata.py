# -*- coding:utf-8 -*-
# 启动入口
# 用户情感分析

import re
import jieba
import pandas as np
import numpy
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib

# 读文件
file1 = open("E:\\reptile\\comm.txt", 'r')
xt = file1.read()
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filedata = re.findall(pattern, xt)
xx = ''.join(filedata)
file1.close()
# 清洗数据
clear = jieba.lcut(xx)
cleared = np.DataFrame({'clear': clear})
# print(clear)
stopwords = np.read_csv("chineseStopWords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'], encoding='GBK')
cleared = cleared[~cleared.clear.isin(stopwords.stopword)]
# print(std)
count_words = cleared.groupby(by=['clear'])['clear'].agg({"num": numpy.size})
# count_words = cleared.groupby(by=['clear'])['clear'].agg(np.size)
# count_words = count_words.to_frame()
# count_words.columns = ['num']

count_words = count_words.reset_index().sort_values(by=["num"], ascending=False)
# print(count_words)
# 词云展示
wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=250, width=1300,
                      height=800)  # 指定字体类型、字体大小和字体颜色
word_frequence = {x[0]: x[1] for x in count_words.head(200).values}
wordcloud = wordcloud.fit_words(word_frequence)
plt.imshow(wordcloud)
plt.axis("off")
plt.colorbar()  # 颜色条
plt.show()

# wctext = open('E:\\pachong1\\comm1.txt', 'r')
print("finish")