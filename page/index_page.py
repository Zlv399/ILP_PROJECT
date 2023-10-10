"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:index_page.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 22:00
"""

from page.base_page import BasePage
from locators.index_loc import IndexLocators as loc

class IndexPage(BasePage):
    """
    系统首页操作的封装
    """


    # def get_index_user_txt(self):
    #     """
    #     获取首页登录用户信息
    #     :return: 返回首页用户登录信息
    #     """
    #     index_user = self.wait_element_visible(loc.t_index_user_ele).text
    #     return index_user

    # def get_index_user_txt(self):
    #     """
    #     获取首页登录用户信息
    #     :return: 返回首页用户登录信息
    #     """
    #     try:
    #         self.wait_element_visible(loc.t_index_user_ele,5)
    #         return True
    #     except Exception:
    #         return False
