from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException,TimeoutException


import time

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()


#  详细学习Selenium用法
# Selenium支持非常多的浏览器，如Chrome,Firefox,Edge等，还有安卓，黑莓等手机端的浏览器
# 也支持无界面浏览器PhantomJS

# 我们可以用如下方式初始化
ch_browser = webdriver.Chrome()
# ff_browser = webdriver.Firefox()
# edge_browser = webdriver.Edge()
# ph_browser = webdriver.PhantomJS()
# sf_browser = webdriver.Safari()

# 访问页面
# ch_browser.get('https://www.taobao.com')

# 打印出网页源码
# print(ch_browser.page_source)

# 查找节点
# input_first = ch_browser.find_element_by_id('q')
# input_second = ch_browser.find_element_by_css_selector('#q')
# input_third = ch_browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first)
# print(input_second)
# print(input_third)

# Selenium提供了通用方法find_element(),他需要传入两个参数，查找方式By和值
# 如果是查多个节点，这个只能返回一个值
# first = ch_browser.find_element(By.ID,'q')
# print(first)

# 查找淘宝左边栏的所有条目

# ch_browser.get('https://www.taobao.com')
# lis = ch_browser.find_elements_by_css_selector('.service-bd li')
# print(lis)

# 节点交互
# input = ch_browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = ch_browser.find_element_by_class_name('btn-search')
# button.click()

# 动作链,用谷歌浏览器有问题，用火狐可以
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# ff_browser.get(url)
# ff_browser.switch_to.frame('iframeResult')
# source = ff_browser.find_element_by_css_selector('#draggable')
# target = ff_browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(ff_browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 执行JavaScript
# ch_browser.get('https://www.zhihu.com/explore')
# ch_browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# ch_browser.execute_script('alert("To Bottom")')

# 获取节点信息
# url = 'https://www.zhihu.com/explore'
# ch_browser.get(url)
# logo = ch_browser.find_element_by_id('zh-top-link-logo')
# print(logo)
# print(logo.get_attribute('class'))

# 获取文本取值
# url = 'https://www.zhihu.com/explore'
# ch_browser.get(url)
# input = ch_browser.find_element_by_class_name('zu-top-add-question')
# print(input.text)

# 获取id，位置，标签名和大小
# url = 'https://www.zhihu.com/explore'
# ch_browser.get(url)
# input = ch_browser.find_element_by_class_name('zu-top-add-question')
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)


# 切换Frame
# ff_browser = webdriver.Firefox()
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# ff_browser.get(url)
# ff_browser.switch_to.frame('iframeResult')
# try:
#     logo = ff_browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print("No LOGO")
# ff_browser.switch_to.parent_frame()
# logo = ff_browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 延时等待

# 隐式等待
# ch_browser.implicitly_wait(10)
# ch_browser.get('https://www.zhihu.com/explore')
# input = ch_browser.find_element_by_class_name('zu-top-add-question')
# print(input)

# 显式等待
# ch_browser.get('https://www.taobao.com')
# wait = WebDriverWait(ch_browser,10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

#  前进和后退
# ch_browser.get('https://www.baidu.com/')
# ch_browser.get('https://www.taobao.com/')
# ch_browser.get('https://www.python.org/')
# ch_browser.back()
# time.sleep(1)
# ch_browser.forward()

# Cookies
# ch_browser.get('https://www.zhihu.com/explore')
# print(ch_browser.get_cookies())
# ch_browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germey'})
# print(ch_browser.get_cookies())
# ch_browser.delete_all_cookies()
# print(ch_browser.get_cookies())

# 选项卡
# ch_browser.get('https://www.baidu.com')
# ch_browser.execute_script('window.open()')
# print(ch_browser.window_handles)
# ch_browser.switch_to.window(ch_browser.window_handles[1])
# ch_browser.get('https://www.taobao.com')
# time.sleep(1)
# ch_browser.switch_to.window(ch_browser.window_handles[0])
# ch_browser.get('https://python.org')

# 异常处理
# ch_browser.get('https://www.baidu.com')
# ch_browser.find_element_by_id('hello')

# try:
#     ch_browser.get('https://www.baidu.com')
# except TimeoutException:
#     print('Time Out')
# try:
#     ch_browser.find_element_by_id('hello')
# except NoSuchElementException:
#     print('No Element')
# finally:
#     ch_browser.close()


# ch_browser.close()


