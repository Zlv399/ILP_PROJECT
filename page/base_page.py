"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:base_page.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/13 22:40
"""

import os
import time
from config.config import IMAGE_PATH
from datetime import datetime
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage(object):

    """
    基类，二次封装selenium中常用的操作
    """
    # 函数注解,指定参数 driver 的预期类型为 Chrome
    def __init__(self,driver:Chrome):
        """
        初始化driver
        :param driver:driver对象
        :return:
        """
        self.driver = driver


    def find(self,locator):
        """
        查找元素方法，显示等待，并判断元素定位方式，并返回元素对象
        :param locator:元素定位方式、定位数据
        :return:
        """
        # try:
        #     find = WebDriverWait(self.driver, timeout, 0.5).until(lambda x: x.find_element(*locator))
        # except Exception as err:
        #     logging.error(err)
        #     self.save_screenshot()
        # else:
        #     return find
        try:
            e = self.driver.find_element(*locator)
        except Exception as err:
            # 没有找到元素
            # logging.error(f"元素定位失败：{err}")
            # 截图
            self.save_screenshot()
            raise err
        else:
            return e


    def finds(self,locator):
        """
        查找多个元素方法，并将所有元素以列表返回
        :param locator: 元素定位方式、定位数据
        :return:
        """
        try:
            ele_s = self.driver.find_elements(*locator)
        except Exception as err:
            self.save_screenshot()
            raise err
        else:
            return ele_s

    def save_screenshot(self):
        """截图操作"""

        # existing_files = os.listdir(IMAGE_PATH)
        # for file in existing_files:
        #     file_path = os.path.join(IMAGE_PATH, file)
        #     if os.path.isfile(file_path):
        #         os.remove(file_path)
        # 路径拼接
        # 时间戳命名，防止覆盖
        ts_str = time.strftime('%y%m%d-%H_%M_%S')
        file_name = os.path.join(IMAGE_PATH, ts_str) + '.png'
        self.driver.save_screenshot(file_name)
        # 将当前对象自身作为结果返回，使得该方法可以链式调用，即在调用完 save_screenshot()方法后继续调用其他方法，无需单独的变量引用。
        return self

    def wait_element_clickable(self,locator,timeout=10,poll_frequency=0.2):
        """
        等待元素可以被点击，等待失败截图
        :param locator: 元素定位
        :param timeout: 指定等待时间，默认20s
        :param poll_frequency: 指定轮询间隔时间，默认0.2s一次
        :return:
        """
        wait = WebDriverWait(self.driver,timeout,poll_frequency)
        try:
            e = wait.until(EC.element_to_be_clickable(locator))
        except Exception as err:
            #可以加上日志处理
            self.save_screenshot()
            raise err
        else:
            return e

    def wait_element_visible(self,locator,timeout=10,poll_frequency=0.2):
        """
        等待元素可见，等待失败截图
        :param locator: 元素定位
        :param timeout: 指定等待时间默认20s
        :param poll_frequency: 指定轮询间隔时间，默认0.2s一次
        :return:
        """
        wait = WebDriverWait(self.driver,timeout,poll_frequency)
        try:
            e = wait.until(EC.visibility_of_element_located(locator))
        except Exception as err:
            #可以加上日志处理
            self.save_screenshot()
            raise err
        else:
            return e
    def wati_element_invisibility(self,locator,timeout=6,poll_frequency=0.2):
        """
        等待元素不可见，等待失败截图
        :param locator: 元素定位
        :param timeout: 指定等待时间默认6s
        :param poll_frequency: 指定轮询间隔时间，默认0.2s一次
        :return:
        """
        wait = WebDriverWait(self.driver,timeout,poll_frequency)
        try:
            e = wait.until(EC.invisibility_of_element_located(locator))
        except Exception as err:
            self.save_screenshot()
            raise err




    def wait_element_present(self,locator,timeout=10,poll_frequency=0.2):
        """
        等待元素被加载，等待失败截图
        :param locator: 元素定位信息
        :param timeout: 指定等待时间，默认20s
        :param poll_frequency: 指定轮询间隔时间，默认0.2s一次
        :return:
        """
        wait = WebDriverWait(self.driver,timeout,poll_frequency)
        try:
            e = wait.until(EC.presence_of_element_located(locator))
        except Exception as err:
            #可以加上日志处理
            self.save_screenshot()
        else:
            return e


    def click(self,locator):
        """
        点击元素
        :param locator:元素定位信息
        :return:
        """
        try:
            click = self.find(locator)
            click.click()
        except Exception as err:
            #可以加上日志处理
            self.save_screenshot()
        return self

    def double_click(self,locator):
        """
        双击元素
        :param locator:
        :return:
        """
        actions = ActionChains(self.driver)
        actions.double_click(locator).perform()

    def send_value(self,locator,txt):
        """
        操作输入框，清空输入框内容，指定输入文本
        通过执行js脚本点击该元素
        Webdriver对部分浏览器上的控件时不支持直接驱动的，例如滚动条、时间控件，所以需要执行JS脚本，间接完成这些操作
        :param locatot: 元素定位
        :param txt: 指定需要输入的文本值
        :return:
        """
        try:
            # send_value = self.driver.find_element(*locator)
            # send_value = self.find(locator)
            # send_value = self.wait_element_visible(locator)
            # send_value = self.wait_element_clickable(locator)
            send_value =self.find(locator)
            #解决元素点击被拦截的异常ElementClickInterceptedException
            self.driver.execute_script("arguments[0].click();", send_value)
            send_value.clear()
            send_value.send_keys(txt)
        except Exception as err:
            #可以加上日志处理
            self.save_screenshot()
            raise err
        #将当前对象作为返回值返回,这样做的目的是为了支持链式调用（链式操作）
        return self

    def get_title(self):
        """
        获取当前窗口标题
        :return:
        """
        title = self.driver.title
        return title

    def get_text(self,locator):
        """
        获取元素的文本内容
        :param locator: 元素定位
        :return:
        """
        text = self.find(locator).text
        return text

    def move_to_element(self,locator):
        """
        鼠标移动到元素上（悬停），悬停后面可以链式调用其它方法，比如click等
        ActionChains(self.driver).move_to_element(el).click(el).perform()
        当调用 perform() 方法时，Selenium 会将 ActionChains 对象中的操作转换为底层浏览器驱动可以理解的命令，并发送给浏览器执行
        :param locator: 元素定位
        :return:
        """
        el = self.find(locator)
        # move_to_element(el) 后面可以链式调用其他方法，如 .click(), .double_click()
        ActionChains(self.driver).move_to_element(el).perform()

    def select_to_value(self,locator,value):
        """
        下拉框操作(选中)，通过value值选择
        :param locator: 元素定位
        :param value: 指定value值
        :return:
        """
        webelement = self.find(locator)
        Select(webelement).select_by_value(value)

    def select_to_index(self,locator,index):
        """
        下拉框操作(选中)，通过index索引选择
        :param locator: 元素定位
        :param index: 索引值，整数类型
        :return:
        """
        webelement = self.find(locator)
        Select(webelement).select_by_value(index)

    def select_to_text(self,locator,text):
        """
        下拉框操作(选中)，通过text文本值选择
        :param locator: 元素定位
        :param text: 指定text文本值
        :return:
        """
        webelement = self.find(locator)
        Select(webelement).select_by_visible_text(text)

    def js(self, script):
        """
        执行JavaScript脚本.
        用法: driver.js("window.scrollTo(200,1000);")
        :param script: JavaScript脚本
        :return:
        """
        self.driver.execute_script(script)

    def window_scroll_to(self, left='0', top='0'):
        """
        控制浏览器滚动条的位置
        :param left: 水平的左边距
        :param top: 垂直的上边距
        Usage:
            window_scroll_to(100, 0)  #右滑
            execute_script("window.scrollTo(document.body.scrollWidth, 0)");
            window_scroll_to(0, 100)  #下滑
            execute_script("window.scrollTo(0, document.body.scrollHeight)");
        """
        scroll = "window.scrollTo(%s, %s);" % (left, top)
        self.js(scroll)

