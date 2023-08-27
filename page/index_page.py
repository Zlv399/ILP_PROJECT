"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:index_page.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 22:00
"""

from page.base_page import BasePage
from selenium.webdriver.common.by import By

class IndexPage(BasePage):
    """
    系统首页操作的封装
    """
    #t = 文本信息
    t_index_user_locator = (By.XPATH,'//*[@id="avue-view"]/div/div[1]/div[1]/div[2]/p/span')

    def get_index_user_txt(self):
        """
        获取首页登录用户信息
        :return: 返回首页用户登录信息
        """
        index_user = self.wait_element_visible(self.t_index_user_locator).text
        return index_user


