from urllib import request
from bs4 import BeautifulSoup
import re
import os

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) App' 
                       'leWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
}
content_url = "https://www.booktxt.net/1_1239/"  # 小说目录链接
url = content_url[:re.search(".com", content_url).span()[1]]  # 网站链接


def get_link():
    req = request.Request(content_url, headers=header)
    html = request.urlopen(req).read()
    result = html.decode("gbk")  # 用某种编码方式解释网页
    soup = BeautifulSoup(result, 'lxml')
    dl = soup.find('dl')

    start_tag = False
    for item in dl.contents:
        if item == '\n':
            continue
        elif item.string == u"《神墓》正文卷":
            start_tag = True
        elif start_tag:
            print(item.string + ":" + url + item.a["href"])
            get_content(item.string, url + item.a["href"])


def get_content(title, text_url):
    chapter_req = request.Request(text_url, headers=header)
    html = request.urlopen(chapter_req).read()
    result = html.decode("gbk")
    soup = BeautifulSoup(result, "lxml")
    div_content = soup.find(attrs={"class": "showtxt", "id": "content"})  # 找到小说正文部分的元素

    if "xiedu" not in os.listdir("./myProject/utllib"):
        os.makedirs("./myProject/utllib/xiedu")
    txt_file = open("./myProject/utllib/xiedu/" + title + ".txt", "w", encoding='utf-8')  # 打开文件，不存在则创建
    lines = re.sub('[\xa0]+', "\r\n\r\n", div_content.text)  # 将'\xa0'替换为换行符
    lines = lines[:re.search(";?\[[笔趣看]?", lines).span()[0]]  # 去掉文章末尾不需要的内容
    txt_file.writelines(lines)  # 写数据到文件


if __name__ == "__main__":
    get_link()
