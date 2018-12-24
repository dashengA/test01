from appium.webdriver.common.touch_action import TouchAction

from base import base_driver


class BaseAciton:
    #当类初始化的时候这个方法就执行
    def __init__(self,driver):
        self.driver = driver

    #把一些常见的操作定义出来 (点击 输入内容)
    def click_element(self,loc):
        #到底点击哪个元素 是不是的先找到这个元素才能点击
        self.find_element(loc).click()

    def input_element_content(self,loc,content):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)


    """
      loc代表要传递一个元祖进来 返回找到的元素
    """
    def find_element(self, loc):
        #在找元素之前 等待
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])

