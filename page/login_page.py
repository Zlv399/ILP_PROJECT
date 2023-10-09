"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:login_page.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 20:14
"""
import time

from config.config import TEST_HOST
from page.base_page import BasePage
from locators.login_loc import LoginLocators as loc




class LoginPage(BasePage):
    """
    登录页面操作的封装
    1、访问登录页面
    2、登录操作：定位用户名、输入账号，定位密码、输入密码，定位登录按钮、点击登录
    3、获取页面报错信息
    """
    login_url = TEST_HOST + '#/login'

    def get_login(self):
        """
        访问登录页面
        :return:
        """
        self.driver.get(self.login_url)
        return self

    def login(self,name,pwd):
        """
        输入账号密码，进行登录操作
        白名单，跳过图形验证码
        :param name: 账号
        :param pwd: 密码
        :return:
        """
        # self.move_to_element(self.i_user_locator)
        self.send_value(loc.i_user_ele, name)
        self.send_value(loc.i_pwd_ele,pwd)
        self.click(loc.bt_login_ele)

    # def get_input_user_error(self):
    #     """
    #     获取用户名输入框的报错信息
    #     :return:
    #     """
    #     user_err = self.wait_element_visible(loc.ier_user_ele).text
    #     return user_err
    #     # if user_err.is_displayed():
    #     #     return user_err.text
    #     # elif pwd_err.is_displayed():
    #     #     return pwd_err.text
    #     # user_err = self.wati_element_visible(self.user_err_locator)
    #     # pwd_err = self.wati_element_visible(self.pwd_err_locator)
    #
    # def get_input_pwd_error(self):
    #     """
    #     获取密码输入框的报错信息
    #     :return:
    #     """
    #     # pwd_err = self.find(self.pwd_err_locator).text
    #     pwd_err = self.wait_element_visible(loc.ier_pwd_ele).text
    #     return pwd_err
    #
    # def get_prompt_error(self):
    #     """
    #     获取页面弹窗提示的错误信息
    #     :return:
    #     """
    #     pormpt_err = self.wait_element_visible(loc.p_login_err_ele).text
    #     return pormpt_err
