"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:read_element_yaml.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/9/11 0:32
"""

import yaml
import os
from config.config import ELEMENT_PATH

class ElementInfo():
    """
    读取维护元素定位信息的yaml文件
    """
    def __init__(self, file_name):
        """
        初始化文件路径以及文件名称，并读取文件
        :param file_name:
        """
        self.file_name = '%s.yaml' % file_name
        self.file_path = os.path.join(ELEMENT_PATH,self.file_name)
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("%s 文件不存在！" % self.file_path)
        with open(self.file_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, key):
        """获取元素定位属性"""
        #获取yaml文件中，对应键的值
        data = self.data.get(key)
        if data:
            #以元组方式返回
            return tuple(data.values())
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, key))


