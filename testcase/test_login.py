"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:test_login.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 21:20
"""
import time

import pytest
import allure
from page.login_page import LoginPage
from page.index_page import IndexPage
from common.read_testdata_yaml import ReadYamlDataInfo



@allure.feature('登录模块')
@allure.story('登录测试')
class TestLogin():

    #读取测试数据
    test_data = ReadYamlDataInfo('login_data')

    @allure.title('账号为空登录')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('test_info',test_data['cases_user_none'])
    def test_login_user_none_err(self,test_info,browser):
        """
        用户名为空登录
        :param test_info:登录参数
        :param browser: fixture函数，返回driver对象
        :return:
        """
        login = LoginPage(browser)
        with allure.step('进入登录页面，输入账号密码，操作登录'):
            login.get_login().login(test_info['username'],test_info['password'])
        with allure.step('获取登录失败提示信息'):
            login_user_err = login.get_input_user_error()
        assert test_info['expected'] == login_user_err


    @allure.title('密码为空登录')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('test_info',test_data['cases_pwd_none'])
    def test_login_pwd_none_err(self,test_info,browser):
        """
        密码为空登录
        :param test_info:登录参数
        :param browser: fixture函数，返回dirver对象
        :return:
        """
        login = LoginPage(browser)
        with allure.step('输入账号密码，操作登录'):
            login.get_login().login(test_info['username'],test_info['password'])
        with allure.step('获取登录失败提示信息'):
            login_pwd_err = login.get_input_pwd_error()
        assert test_info['expected'] == login_pwd_err


    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('test_info',test_data['cases_error'])
    def test_login_err(self,test_info,browser):
        """
        账号密码错误，两种情况登录；图形验证码白名单绕过，所以密码错误断言使用验证码错误提示
        :param test_info: 登录参数
        :param browser: fixture函数，返回driver对象
        :return:
        """
        login = LoginPage(browser)
        #参数化生成用例标题
        allure.dynamic.title(test_info['testcase_title'])
        with allure.step('输入账号密码，操作登录'):
             login.get_login().login(test_info['username'],test_info['password'])
        with allure.step('获取登录失败提示信息'):
             login_err = login.get_prompt_error()
        assert test_info['expected'] == login_err


    @allure.title('账号密码正确登录')
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('test_info',test_data['cases_success'])
    def test_login(self,test_info,browser):
        """
        正常登录
        :param test_info:登录参数
        :param browser: fixture函数，返回driver对象
        :return:
        """
        login = LoginPage(browser)
        with allure.step('输入账号密码，操作登录'):
             login.get_login().login(test_info['username'],test_info['password'])
        with allure.step('获取首页登录用户信息'):
             user = IndexPage(browser).get_index_user_txt()
        assert test_info['expected'] in user