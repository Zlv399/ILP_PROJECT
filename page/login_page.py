"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:login_page.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 20:14
"""
from config.config import TEST_HOST
from page.base_page import BasePage
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """
    登录页面操作的封装
    1、访问登录页面
    2、登录操作：定位用户名、输入账号，定位密码、输入密码，定位登录按钮、点击登录
    3、获取页面报错信息
    """
    # i：输入框  bt：按钮  t：文本属性 p:弹窗提示 ier:输入框异常提示
    login_url = TEST_HOST + '#/login'
    i_user_locator = (By.XPATH,'//input[@autocomplete="off"][@placeholder="请输入账号"]')
    i_pwd_locator = (By.XPATH,'//input[@autocomplete="off"][@type="password"]')
    bt_login_locator = (By.XPATH,'//button[@type="button"][@class="el-button login-submit el-button--primary el-button--small"]')
    ier_user_locator = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div/form/div[2]/div/div[2]')
    ier_pwd_locator = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div/form/div[3]/div/div[2]')
    p_login_err_locator = (By.XPATH,'//p[@class="el-message__content"]')

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
        # self.move_to_element(self.i_user_locator
        self.send_value(self.i_user_locator,name)
        self.send_value(self.i_pwd_locator,pwd)
        self.click(self.bt_login_locator)

    def get_input_user_error(self):
        """
        获取用户名输入框的报错信息
        :return:
        """
        user_err = self.wait_element_visible(self.ier_user_locator).text
        return user_err
        # if user_err.is_displayed():
        #     return user_err.text
        # elif pwd_err.is_displayed():
        #     return pwd_err.text
        # user_err = self.wati_element_visible(self.user_err_locator)
        # pwd_err = self.wati_element_visible(self.pwd_err_locator)

    def get_input_pwd_error(self):
        """
        获取密码输入框的报错信息
        :return:
        """
        # pwd_err = self.find(self.pwd_err_locator).text
        pwd_err = self.wait_element_visible(self.ier_pwd_locator).text
        return pwd_err

    def get_prompt_error(self):
        """
        获取页面弹窗提示的错误信息
        :return:
        """
        pormpt_err = self.wait_element_visible(self.p_login_err_locator).text
        return pormpt_err
