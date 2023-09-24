"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:index_loc.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/9/5 23:57
"""
from selenium.webdriver.common.by import By

class IndexLocators:
    """
    1、首页登录用户信息
    """
    # i：输入框  bt：按钮  t：文本属性 p:弹窗提示 ier:输入框异常提示
    t_index_user_ele = (By.XPATH, '//*[@id="avue-view"]/div/div/div[1]/div[1]/div[2]/p/span')