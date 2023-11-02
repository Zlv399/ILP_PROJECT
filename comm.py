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