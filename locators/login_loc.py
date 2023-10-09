"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:login_loc.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/9/5 23:42
"""
from selenium.webdriver.common.by import By

class LoginLocators:
    """
    登录页面元素定位信息
    1、账号输入框
    2、密码输入框
    3、登录按钮
    4、账号为空错误提示信息
    5、密码为空错误提示信息
    6、阻断提示弹窗
    """
    # i：输入框  bt：按钮  t：文本属性 p:弹窗提示 ier:输入框异常提示
    i_user_ele = (By.XPATH,'//input[@autocomplete="off"][@placeholder="请输入账号"]')
    i_pwd_ele = (By.XPATH,'//input[@autocomplete="off"][@type="password"]')
    bt_login_ele = (By.XPATH,'//button[@type="button"][@class="el-button login-submit el-button--primary el-button--small"]')
    # ier_user_ele = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div/form/div[2]/div/div[2]')
    # ier_pwd_ele = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div/form/div[3]/div/div[2]')
    # p_login_err_ele = (By.XPATH,'//p[@class="el-message__content"]')