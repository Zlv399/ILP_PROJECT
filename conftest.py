"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:conftest.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/10 12:00
"""
import os
import pytest,allure
import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.config import IMPLICTLY_WAIT_TIMEOUT,IMAGE_PATH
from page.login_page import LoginPage
from common.read_testdata_yaml import ReadYamlDataInfo

driver = None
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
    global driver
    if driver == None:
    #解决ssl协议握手报错ERROR:ssl_client_socket_impl.cc(962)] handshake failed；returned -1, SSL error code 1
        chrome_options = Options()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_experimental_option('excludeSwitches', ['ignore-certificate-errors'])
    #将窗口最大化作为chrome的启动选项，即启动浏览器时就是最大化
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(IMPLICTLY_WAIT_TIMEOUT)
    # driver.maximize_window()
        yield driver
        driver.quit()

@pytest.fixture(scope='class')
def login(browser):
    """
    实现执行用例前的登录操作
    :param browser:driver对象
    :return:driver对象
    """
    user = ReadYamlDataInfo('login_data')
    login = LoginPage(browser)
    login.get_login().login(user['login']['username'],user['login']['password'])
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

def pytest_collection_modifyitems(items):
    """
    解决控制台输出用例id中文编码错误问题
    :param items:
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    hook pytest allure用例失败截图
    :param item:
    :return:
    """
    # 获取钩子方法的调用结果
    outcome = yield
    # 从钩子方法的调用结果中获取测试报告
    rep = outcome.get_result()
    # print(rep,'调试')
    # rep.when表示测试步骤，仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加报告截图
        with allure.step('查看失败截图'):
             #需要先实例化一个driver，才能用到driver的截图方法
            allure.attach(driver.get_screenshot_as_png(), "失败截图",
            allure.attachment_type.PNG)