"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:read_testdata_yaml.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/9/4 22:38
"""

import time
import yaml
import os
from config.config import TESTDATA_PATH
from string import Template

class ReadYamlDataInfo():
    """
    读取维护元素定位信息的yaml文件
    """
    def __init__(self, file_name):
        """
        初始化文件路径以及文件名称，并读取文件
        :param file_name:
        """
        self.file_name = '%s.yaml' % file_name
        self.file_path = os.path.join(TESTDATA_PATH,self.file_name)
        if not os.path.exists(self.file_path):
            raise FileNotFoundError("%s 文件不存在！" % self.file_path)
        with open(self.file_path, encoding='utf-8') as f:
            self.textdata = f.read()
            # self.yamldata = yaml.safe_load(f),在使用了read方法后不能直接解析文件对象f，因为read方法在调用后会将文件指针移动到文件末尾
            # 文件指针已经在末尾位置，没有剩余的内容可供解析
            self.yamldata = yaml.safe_load(self.textdata)

    def __getitem__(self, key):
        """获取yaml文件维护的测试数据"""
        #通过字典键，获取yaml文件中，字典的值
        data  = self.yamldata.get(key)
        if data:
            #返回格式根据yaml文件维护的格式决定
            return data
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, key))

    def yaml_replace(self,data: dict):
        """
        替换yaml文件中的环境变量
        :param data: 替换的变量数据、字典 格式为 变量名：替换后的值
        :return:
        """
        yaml_replace = Template(self.textdata).substitute(data)
        return yaml.safe_load(yaml_replace)


