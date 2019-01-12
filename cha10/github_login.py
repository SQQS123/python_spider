import requests
from lxml import etree

class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com',
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    # 实现一个token()方法
    def token(self):
        response = self.session.get(self.login_url,headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')[0]
        return token

    # 实现登录功能
    def login(self,email,password):
        post_data = {
            'commit':'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url,data=post_data,headers=self.headers)
        print(response)
        if response.status_code == 200:
            print("登录成功")
        #     self.dynamics(response.text)
        #
        # response = self.session.get(self.logined_url, headers=self.headers)
        # if response.status_code == 200:
        #     self.profile(response.text)

    # 找不到咯~~~
    # def dynamics(self,html):
    #     selector = etree.HTML(html)
    #     dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class,"alert")]')
    #     for item in dynamics:
    #         dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
    #         print(dynamic)

    # def profile(self,html):
    #     selector = etree.HTML(html)
    #     name = selector.xpath('//input[@id="user_profile_name"]/@value')
    #     email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""/text()')
    #     print(name,email)


if __name__ == "__main__":
    login = Login()
    # 填入账号密码登录
    login.login(email='',password='')