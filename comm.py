"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:comm.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/15 23:23
"""
#个人测试文件

# from config.config import ELEMENT_PATH
# import os
# import yaml
# class ReadtInfo():
#     """
#     读取维护元素定位信息的yaml文件
#     """
#     def __init__(self, file_name):
#         """
#         初始化文件路径以及文件名称，并读取文件
#         :param file_name:
#         """
#         self.file_name = '%s.yaml' % file_name
#         self.file_path = os.path.join(ELEMENT_PATH,self.file_name)
#         if not os.path.exists(self.file_path):
#             raise FileNotFoundError("%s 文件不存在！" % self.file_path)
#         with open(self.file_path, encoding='utf-8') as f:
#             self.data = yaml.safe_load(f)

import pytest

class Authenticator:
    def username_password_authenticate(self, username, password):
        # 模拟用户名密码认证逻辑
        if username == "user1" and password == "pass123":
            return True
        else:
            return False

    def social_media_authenticate(self, social_name, social_type):
        # 模拟社交媒体认证逻辑
        if social_name == "zhangsan" and social_type == 'Tiktok':
            return True
        else:
            return False

@pytest.fixture
def authentication_method(request):
    # 根据参数选择认证方式
    method = request.param
    if method == 'username_password':
        return Authenticator().username_password_authenticate
    elif method == 'social_media':
        return Authenticator().social_media_authenticate

@pytest.mark.parametrize('authentication_method', ['username_password','social_media'],indirect=True)
def test_login(authentication_method):
    # 在测试函数中使用 authentication_method 进行测试
    result = authentication_method('user1', 'pass123')
    assert result is True