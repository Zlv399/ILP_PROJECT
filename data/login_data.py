"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:login_data.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/14 20:56
"""

"""
登录模块测试数据
"""

cases_success = [
    {'username':'fyx','password':'Fyx10086','expected':'方一一'}
]

cases_user_none = [
    {'username': '', 'password': 'Fyx10086', 'expected': '请输入用户名'}
]

cases_pwd_none = [
    {'username': 'fyx', 'password': '', 'expected': '请输入密码'}
]

cases_error = [
    {'testcase_title':'密码错误登录','username': 'fyx', 'password': '100861', 'expected': '用户名或密码错误'},
    {'testcase_title':'账号错误登录','username': 'fyxsdd', 'password': 'Fyx10086', 'expected': '验证码不正确'}
]