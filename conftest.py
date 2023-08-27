"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:conftest.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/10 12:00
"""
import os
import pytest
from selenium import webdriver
from data.login_data import cases_success
from config.config import IMPLICTLY_WAIT_TIMEOUT,IMAGE_PATH
from page.login_page import LoginPage

@pytest.fixture(scope='class')
def browser():
    """
    启动和关闭浏览器
    1、初始化浏览器
    2、设置隐式等待时间
    3、最大化浏览器
    4、返回driver对象
    5、关闭浏览器
    :return:
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(IMPLICTLY_WAIT_TIMEOUT)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='class')
def login(browser):
    """
    实现执行用例前的登录操作
    :param browser:driver对象
    :return:driver对象
    """
    login = LoginPage(browser)
    login.get_login().login(cases_success[0]['username'],cases_success[0]['password'])
    yield browser


@pytest.fixture(scope='session',autouse=True)
def clear_screenshots():
    """
    每次测试前，清空截图目录中的图片文件
    """
    if os.path.exists(IMAGE_PATH):
        existing_files = os.listdir(IMAGE_PATH)
        for file in existing_files:
            file_path = os.path.join(IMAGE_PATH, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
