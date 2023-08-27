"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:test_device_category.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/16 23:30
"""

import time

import pytest

from page.device.device_category_page import DeviceCategoryPage
from data.device_data import device_category,select_device_category,update_device_category



class TestDeviceCategory:

    @pytest.mark.parametrize('test_info',device_category)
    def test_save_devca(self,login,test_info):
        """
        新增仪器分类信息
        :param login:fixture函数，返回driver对象
        :param test_info: 仪器分类基本信息参数，字典
        :return:
        """
        device_category = DeviceCategoryPage(login)
        device_category.get_device_category_index()
        save_devca = device_category.save_devicecategory(test_info['device_category_name'],test_info['sort'])
        try:
            assert test_info['expected'] == save_devca
        except Exception as e:
            raise e

    @pytest.mark.parametrize('test_info',select_device_category)
    def test_select_devca(self,login,test_info):
        """
        通过仪器名称，查询仪器分类信息（模糊匹配）
        :param login: fixture函数，返回driver对象
        :param test_info: 仪器分类名称
        :return:
        """
        devca = DeviceCategoryPage(login)
        listone_device = devca.select_devca(test_info['select_devca'])
        try:
            assert test_info['select_devca'] in listone_device
        except Exception as e:
            raise e

    @pytest.mark.parametrize('test_info',update_device_category)
    def test_update_devca(self,login,test_info):
        """
        仪器分类编辑
        :param login:fixture函数，返回driver对象
        :param test_info:仪器分类基本信息编辑，字典
        :return:
        """
        devca = DeviceCategoryPage(login)
        update_devca_p = devca.update_devca(test_info['update_devica_text'])
        try:
            assert test_info['expected'] == update_devca_p
        except Exception as err:
            raise err

