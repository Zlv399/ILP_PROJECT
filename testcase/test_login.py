"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:test_login.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 21:20
"""

import pytest
from data.login_data import cases_success,cases_error,cases_user_none_error,cases_pwd_none_error
from page.login_page import LoginPage
from page.index_page import IndexPage

class TestLogin():

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('test_info',cases_user_none_error)
    def test_login_user_none_err(self,test_info,browser):
        """
        用户名为空登录
        :param test_info:登录参数
        :param browser: fixture函数，返回driver对象
        :return:
        """
        login = LoginPage(browser)
        login.get_login().login(test_info['username'],test_info['password'])
        login_user_err = login.get_input_user_error()
        try:
            assert test_info['expected'] == login_user_err
        except Exception as e:
            raise e

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('test_info',cases_pwd_none_error)
    def test_login_pwd_none_err(self,test_info,browser):
        """
        密码为空登录
        :param test_info:登录参数
        :param browser: fixture函数，返回dirver对象
        :return:
        """
        login = LoginPage(browser)
        login.get_login().login(test_info['username'],test_info['password'])
        login_pwd_err = login.get_input_pwd_error()
        try:
            assert test_info['expected'] == login_pwd_err
        except Exception as e:
            raise e

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('test_info',cases_error)
    def test_login_err(self,test_info,browser):
        """
        账号密码错误，两种情况登录；图形验证码白名单绕过，所以密码错误断言使用验证码错误提示
        :param test_info: 登录参数
        :param browser: fixture函数，返回driver对象
        :return:
        """
        login = LoginPage(browser)
        login.get_login().login(test_info['username'],test_info['password'])
        login_err = login.get_prompt_error()
        try:
            assert test_info['expected'] == login_err
        except Exception as e:
            raise e

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('test_info',cases_success)
    def test_login(self,test_info,browser):
        """
        正常登录
        :param test_info:登录参数
        :param browser: fixture函数，返回driver对象
        :return:
        """
        login = LoginPage(browser)
        login.get_login().login(test_info['username'],test_info['password'])
        user = IndexPage(browser).get_index_user_txt()
        try:
            assert test_info['expected'] in user
        except Exception as e:
            raise e



