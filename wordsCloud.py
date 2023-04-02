import json
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取json文件
with open('danmu_BV12M4y1m7kf.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 获取所有弹幕内容
text = ''
for item in data:
    text += item['text']

# 加载停用词表
stopwords = set()
with open('cn_stopwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.add(line.strip())

# 使用jieba进行分词，去掉停用词
words = [word for word in jieba.cut(text) if word not in stopwords]

# 将分词结果转换为字符串
words_str = ' '.join(words)

# 生成词云
wc = WordCloud(background_color='white', width=1000, height=800, font_path='msyh.ttc')
wc.generate(words_str)

# 显示词云
plt.imshow(wc)
plt.axis('off')
plt.show()
