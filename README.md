# 弹幕词云生成器
Get bullet chat from bilibili.com by crawler and make word cloud

这是一个从 bilibili.com 爬取弹幕并生成词云的 Python 项目

效果预览:

![预览图片](https://raw.githubusercontent.com/vinouno/blog_image/main/danmu_BV12M4y1m7kf-%E9%A2%84%E8%A7%88.png "预览")

## 安装

1. 克隆这个项目
```
git clone git@github.com:vinouno/BilibiliDanmuCrawler.git
cd BilibiliDanmuCrawler
```
2. 使用`conda`命令创建并激活虚拟环境：

```
conda env create -f environment.yml
conda activate wordsCloud
```

## 用法

替换代码中的`bvid`为你想获取弹幕的视频的 bv 号。

运行`python main.py`，弹幕词云图片将会生成在同一目录下。

## 项目详解

流水账解析：

[弹幕词云生成器](https://vinouno.github.io/posts/29fc4cd/)

## 注意事项

- 本项目使用了[jieba](https://github.com/fxsjy/jieba) 中文分词，仅适用于生成中文词云。
- `cn_stopwords.txt`为停用词表，可以按自己的需求编辑或选择新的停用词表。
