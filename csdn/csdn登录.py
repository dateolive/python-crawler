import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = '2448282543@qq.com'
PASSWORD = '密码'
TITLE='模拟登录csdn并发布文章'
ARTICLE='这是一篇水文，爬虫测试'

class CrackTouClick():
    def __init__(self):
        self.url = 'https://passport.csdn.net/login?code=public'
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD
        self.title=TITLE
        self.article=ARTICLE


    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        #进去之后，先要点击账号密码登录，跳过微信登录的页面
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a').click()
        time.sleep(2)
        email = self.wait.until(EC.presence_of_element_located((By.ID, 'all')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'password-number')))
        email.send_keys(self.username)
        time.sleep(2)
        password.send_keys(self.password)
        login_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-primary')))
        # 随机暂停几秒
        time.sleep(random.random() * 3)
        # 点击登陆按钮
        login_btn.click()
    def write(self):
        time.sleep(3)
        self.browser.find_element_by_xpath('//*[@id="csdn-toolbar"]/div/div[3]/div[1]/a').click()
        time.sleep(2)
        self.browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[1]/a[1]/span').click()
        time.sleep(2)
        n = self.browser.window_handles  # 这个时候会生成一个新窗口或新标签页的句柄，代表这个窗口的模拟driver
        print('当前句柄: ', n)  # 会打印所有的句柄
        self.browser.switch_to.window(n[-1])
        delete1=self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[2]/input')))
        delete1.clear()
        time.sleep(1)
        title=self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[2]/input')))
        title.send_keys(self.title)
        time.sleep(2)
        delete2=self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre')))
        delete2.clear()
        time.sleep(2)
        message=self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div[1]/div[2]/pre')))
        message.send_keys(self.article)
        keep=self.wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/button[1]')))
        keep.click()


    def crack(self):
        """
        破解入口
        :return: None
        """
        self.open()
        self.write()

if __name__ == '__main__':
    crack = CrackTouClick()
    crack.crack()