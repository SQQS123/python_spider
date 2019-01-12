import time
import cv2
import numpy as np
from io import BytesIO

from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

LOGINUSERNAME = '749804235@qq.com'
PASSWORD = '741WHITESQ!'
BORDER = 6
INIT_LEFT= 60

class CrackGeetest():
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.loginusername = LOGINUSERNAME
        self.password = PASSWORD

    # 模拟点击
    def get_geetest_button(self):
        button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_radar_tip')))
        # button.click()
        return button
    # 获取一个WebElement对象，调用它的click()方法即可模拟点击
    # button = self.get_geetest_button()
    # button.click()

     # 识别缺口，这里由于极验网站将刚开始的完整图片移除了，所以，，，这里就需要升级了。
    def get_screenshot(self):
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot


    def get_position(self):
        img = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_canvas_slice geetest_absolute')))
        time.sleep(2)
        location = img.location
        size = img.size
        top,bottom,left,right = location['y'],location['y'] + size['height'],location['x'],location['x']+size['width']
        return (top,bottom,left,right)

    def get_geetest_image(self,name='captcha.png'):
        top,bottom,left,right = self.get_position()
        print('验证码位置',top,bottom,left,right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left,top,right,bottom))
        captcha.save(name)
        return captcha

    # 得到滑块，可以
    def get_slider(self):
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    # 点按呼出缺口
    # slider = self.get_slider()
    # slider.click()

    def is_pixel_equal(self,image1,image2,x,y):
        pixel1 = image1.load()[x,y]
        pixel2 = image2.load()[x,y]
        threshold = 60
        if abs(pixel1[0] - pixel2[0]) < threshold and abs(pixel1[1] - pixel2[1]) < threshold and abs(pixel1[2] - pixel2[2]) < threshold:
            return True
        else:
            return False

    def open(self):
        self.browser.get(self.url)
        loginuser = self.wait.until(EC.presence_of_element_located((By.ID,'email')))
        password = self.wait.until(EC.presence_of_element_located((By.ID,'password')))
        loginuser.send_keys(self.loginusername)
        password.send_keys(self.password)

    def get_gap(self,image1):
        left = 60
        # for i in range(left,image1.size[0]):
        #     for j in range(image1.size[1]):
        #         if not self.is_pixel_equal(image1,image2,i,j):
        #             left = i
        #             return left
        left = 91
        return left

    # 模拟拖动
    def get_track(self,distance):
        track = []
        current = 0
        mid = distance * 4 / 5
        t = 0.2
        v = 0
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            v0 = v
            v = v0+a*t
            move = v0*t + 1/2*a*t*t
            current += move
            track.append(round(move))
        return track

    def move_to_gap(self,slider,tracks):
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in tracks:
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def login(self):
        submit = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'login-btn')))
        submit.click()
        time.sleep(10)
        print('登录成功')

    def crack(self):
        self.open()
        button = self.get_geetest_button()
        print(button)
        button.click()
        # 得到图片
        # image1 = self.get_geetest_image('captcha1.png')
        # # 得到控制滑块的东西
        # slider = self.get_slider()
        # # 点击滑块
        # # slider.click()
        # # 得到有缺口的图片（原）
        # # image2 = self.get_geetest_image('captcha2.png')
        # # 通过比较两张图片得到位置
        # gap = self.get_gap(image1)
        # print('缺口位置',gap)
        # # 减去缺口位移
        # gap -= BORDER
        # track = self.get_track(gap)
        # print('滑动轨迹',track)
        # self.move_to_gap(slider,track)
        #
        # success = self.wait.until(
        #     EC.text_to_be_present_in_element((By.CLASS_NAME, 'geetest_success_radar_tip_content'),'验证成功')
        # )
        # print(success)
        #
        # if not success:
        #     self.crack()
        # else:
        #     self.login()


if __name__ == '__main__':
    crack = CrackGeetest()
    crack.crack()

