import random
import time
from io import BytesIO
import requests
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying

USERNAME = '#b站账号'
PASSWORD = '密码'

CHAOJIYING_USERNAME = '超级鹰账号'
CHAOJIYING_PASSWORD = '密码'
CHAOJIYING_SOFT_ID = 907581
CHAOJIYING_KIND = 9004


class CrackTouClick():
    def __init__(self):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 20)
        self.username = USERNAME
        self.password = PASSWORD


    def open(self):
        """
        打开网页输入用户名密码
        :return: None
        """
        self.browser.get(self.url)
        user = self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
        user.send_keys(self.username)
        password.send_keys(self.password)
        login_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.btn.btn-login')))
        # 随机暂停几秒
        time.sleep(random.random() * 3)
        # 点击登陆按钮
        login_btn.click()

    def pick_code(self):
        time.sleep(3)
        pick_img_label = self.browser.find_element_by_css_selector('img.geetest_item_img')  # 获取点触图片标签
        src = pick_img_label.get_attribute('src')  # 获取点触图片链接
        img_content = requests.get(src).content  # 获取图片二进制内容
        f = BytesIO()
        f.write(img_content)
        img0 = Image.open(f)  # 将图片以文件的形式打开，主要是为了获取图片的大小
        scale = [pick_img_label.size['width'] / img0.size[0],
                 pick_img_label.size['height'] / img0.size[1]]  # 获取图片与浏览器该标签大小的比例
        cjy = Chaojiying(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)
        result = cjy.post_pic(img_content, '9005')  # 发送图片并获取结果
        if result['err_no'] == 0:  # 对结果进行分析
            position = result['pic_str'].split('|')  # position = ['110,234','145,247','25,185']
            position = [[int(j) for j in i.split(',')] for i in position]  # position = [[110,234],[145,247],[25,185]]
            for items in position:  # 模拟点击
                ActionChains(self.browser).move_to_element_with_offset(pick_img_label, items[0] * scale[0],
                                                                       items[1] * scale[1]).click().perform()
                time.sleep(1)
            time.sleep(2)
            # 点击登录
            certern_btn = self.browser.find_element_by_css_selector('div.geetest_commit_tip')
            certern_btn.click()
        return cjy, result

    def crack(self):
        """
        破解入口
        :return: None
        """
        self.open()
        self.pick_code()
if __name__ == '__main__':
    crack = CrackTouClick()
    crack.crack()
