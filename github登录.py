import requests
from pyquery import PyQuery as pq


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'
        ## 维持会话，自动处理cookies
        self.session = requests.Session()

    ## 解析出登录所需要的
    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = pq(response.text)
        token = selector('input[name="authenticity_token"]').attr('value')
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        response = self.session.get(self.feed_url, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    ## 关注动态信息
    def dynamics(self, html):
        selector = pq(html)
        dynamics = selector('div[class="d-flex flex-items-baseline"] div')
        dynamics.find('span').remove()
        for item in dynamics.items():
            dynamic = item.text().strip()
            print(dynamic)

    ## 详情页面
    def profile(self, html):
        selector = pq(html)
        name = selector('input[id="user_profile_name"]').attr('value')
        email = selector('select[id="user_profile_email"] option[selected="selected"]').text()
        site=selector('input[id="user_profile_blog"]').attr('value')
        location=selector('input[id="user_profile_location"]').attr('value')
        print(name, email,site,location)

if __name__ == "__main__":
    login = Login()
    email=input("请输入你的github账号")
    password=input("请输入你的密码")
    login.login(email=email, password=password)