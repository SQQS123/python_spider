import json
import requests
from requests.exceptions import RequestException
import re
import time


# 请求
def get_one_page(url):
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like'
                         'Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 分析一个页面，使用正则表达式
# def parse_one_page(html):
#     pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
#                          + '.*?(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
#                          +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</a>',re.S)
#     items = re.findall(pattern,html)
#
#     for item in items:
#         yield {
#             'index':item[0],
#             'image':item[1],
#             'title':item[2],
#             'actor':item[3].strip()[3:],
#             'time':item[4].strip()[5:],
#             'score':item[5] + item[6]
#         }

def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=' + str(offset)
    html = get_one_page(url)
    subjects = json.loads(html)
    tests = subjects['subjects']
    for item in tests:
        print('电影标题:'+item['title'] +'  影片链接:'+item['url'])


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 20)
        time.sleep(1)
