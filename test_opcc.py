import codecs
from opencc import OpenCC
import requests
from lxml import etree
import os
import jieba
from jieba.analyse import extract_tags
requests = requests.Session()

p = requests.get(
    'https://cn.nytimes.com/business/20200715/huawei-uk-5g/',
    headers = {
        'Host': 'cn.nytimes.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
            })

HTML = etree.HTML(p.text)

comment = HTML.xpath('//div[@class="article-paragraph"]')
article = []
for C in comment[2:]:
    D = C.xpath('.//text()')
    [article.append(E) for E in D]
ARTICLE = ''.join(article)

CC = OpenCC('s2tw')

converted = CC.convert(ARTICLE)

jieba.set_dictionary('..\VS\practice\dict.txt.big.txt')

print(list(jieba.cut(converted, cut_all=False)))
# print(extract_tags(converted))