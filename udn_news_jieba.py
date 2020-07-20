import requests
from lxml import etree
import json
import time
import random
import jieba
from jieba.analyse import extract_tags

jieba.set_dictionary('../VS/practice/dict.txt.big.txt')
jieba.analyse.set_stop_words('../VS/practice/stop_word.txt')
requests = requests.Session()
h = {
            'Host': 'udn.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'https://udn.com/news/breaknews/1',
            'DNT': '1',
            'Connection': 'keep-alive'
            
    }

for page in range(1,50):
    rest = random.randint(1,5)
    p = requests.get(
        'https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=8198',
        headers = h,
        params = {
            'page':page,
            'id':'',
            'channelId':'1',
            'cate_id':'0',
            'type':'breaknews',
            'totalRecNo':'8198'
        }
    )

    a = json.loads(p.text)['lists']
    for b in a:
        print('------------------'+b['title']+'------------------')
        print('\r\n')
        p1 = requests.get('https://udn.com'+b['titleLink'],headers = h)
        HTML = etree.HTML(p1.text)
        comment = HTML.xpath('//section[@class="article-content__editor "]//p//text()')
        Article = ''.join(comment)
        print(Article+'\n')
        print(extract_tags(Article, topK = 10, withWeight=True))
        print('\r\n')
    time.sleep(rest)
    
        
