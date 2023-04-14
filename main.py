import json
import os
import requests
import xml.etree.ElementTree as ET
import jieba
from wordcloud import WordCloud

def get_cid(bvid):
    """获取视频cid"""
    url = 'https://api.bilibili.com/x/web-interface/view?bvid={}'.format(bvid)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
        'Referer': 'https://www.bilibili.com/video/{}'.format(bvid)
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    pages = data['data']['pages']
    cids = []
    for page in pages:
        cids.append(page['cid'])
    return cids

    """
    # 将Python对象转化为JSON格式的字符串，并输出
    print(json.dumps(data, indent=4, ensure_ascii=False))
    print(cid)
    """

def get_danmu(cid):
    """获取弹幕"""
    url = 'https://comment.bilibili.com/{}.xml'.format(cid)
    response = requests.get(url)
    xml_content = response.content.decode('utf-8')
    root = ET.fromstring(xml_content)
    danmu_list = []
    for d in root.iter('d'):
        danmu = d.text
        p_attrs = d.attrib['p']
        p_attrs_list = p_attrs.split(',')
        danmu_dict = {
            'text': danmu,
            'time': float(p_attrs_list[0]),
            'mode': int(p_attrs_list[1]),
            'fontsize': int(p_attrs_list[2]),
            'color': int(p_attrs_list[3]),
            'timestamp': int(p_attrs_list[4]),
            'pool': int(p_attrs_list[5]),
            'userid': p_attrs_list[6],
            'rowid': int(p_attrs_list[7]),
            'duration': int(p_attrs_list[8]),
        }
        danmu_list.append(danmu_dict)
    return danmu_list

def word_cloud_generator(json_name):
    # 读取json文件
    with open(json_name, 'r', encoding='utf-8') as f:
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

    """
    # 显示词云
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    """

    # 保存词云
    filename = os.path.splitext(json_name)[0] + '.png'
    wc.to_file(filename)

if __name__ == '__main__':
    bvid = 'BV1xc41157mK' # 将BV1RK41117gZ替换成你需要获取弹幕的视频的bv号
    cid_list = get_cid(bvid)
    print(cid_list)
    for i, cid in enumerate(cid_list):
        danmu_list = get_danmu(cid)
        json_name = 'danmu_'+ bvid + '_ p'+ str(i+1) +'.json'
        with open(json_name, 'w', encoding='utf-8') as f:
            json.dump(danmu_list, f, ensure_ascii=False, indent=4)
        word_cloud_generator(json_name)
