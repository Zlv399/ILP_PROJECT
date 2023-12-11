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
import allure
from page.device.device_category_page import DeviceCategoryPage
from common.read_testdata_yaml import ReadYamlDataInfo


@allure.feature('仪器模块')
@allure.story('仪器分类')
class TestDeviceCategory:

    #读取测试用例的参数，并将动态参数的占位符替换
    test_info = ReadYamlDataInfo('device_data/device_category')
    replace_data = {
        'nowtime': time.strftime('%y%m%d-%H:%M:%S')
    }
    replaces = test_info.yaml_replace(replace_data)

    @allure.title('新增仪器分类')
    @pytest.mark.parametrize('test_info',replaces['device_category'])
    def test_save_devca(self,login,test_info):
        """
        新增仪器分类信息
        :param login:fixture函数，返回driver对象
        :param test_info: 仪器分类基本信息参数，字典
        :return:
        """
        device_category = DeviceCategoryPage(login)
        with allure.step('进入仪器分类菜单'):
            device_category.get_device_category_index()
        with allure.step('新增仪器分类，获取页面提示语'):
            save_devca = device_category.save_devicecategory(test_info['devca_name'],test_info['sort'])
        assert test_info['expected'] == save_devca

    @allure.title('查询仪器分类')
    @pytest.mark.parametrize('test_info',replaces['select_device_category'])
    def test_select_devca(self,login,test_info):
        """
        通过仪器名称，查询仪器分类信息（模糊匹配）,并重置
        :param login: fixture函数，返回driver对象
        :param test_info: 仪器分类名称
        :return:
        """
        devca = DeviceCategoryPage(login)
        with allure.step('等待上一个操作完成后的页面提示语消失'):
            pass
        with allure.step('查询仪器分类信息'):
            listone_device = devca.select_devca(test_info['select_devca'])
        with allure.step('重置查询条件'):
            devca.restting_devca()
        assert test_info['select_devca'] in listone_device

    @allure.title('编辑仪器分类')
    @pytest.mark.parametrize('test_info',replaces['update_device_category'])
    def test_update_devca(self,login,test_info):
        """
        仪器分类编辑
        :param login:fixture函数，返回driver对象
        :param test_info:仪器分类基本信息编辑，字典
        :return:
        """
        devca = DeviceCategoryPage(login)
        with allure.step('通过仪器分类名称搜索，并编辑第一条分类结果的备注'):
            devca.wati_invisibility()
            update_devca_p = devca.update_devca(test_info['select_devca'],test_info['update_devca_text'])
        with allure.step('编辑完成后重置列表'):
            devca.restting_devca()
        assert test_info['expected'] == update_devca_p


    @allure.title('删除仪器分类')
    @pytest.mark.parametrize('test_info', replaces['remove_device_category'])
    def test_remove_devca(self,test_info,login):
        """
        仪器分类删除
        :param login:fixture函数，返回driver对象
        :return:
        """
        devca = DeviceCategoryPage(login)
        with allure.step('等待上一个操作完成后的提示语消失'):
            #因为客户端时间和服务器时间存在差异所有用等待不可见会出现ssl握手错误，影响元素等待不可见方法，使用强制等待
            # time.sleep(3)
            devca.wati_invisibility()
        with allure.step('通过分类名称搜索分类，并删除第一条分类结果'):
            remove_devca = devca.remove_devca(test_info['select_devca'])
        assert test_info['expected'] == remove_devca

