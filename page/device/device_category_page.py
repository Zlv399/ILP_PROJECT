"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:device_category_page.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/16 23:11
"""
import time
from page.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.device.device_category_loc import DeviceCategoryLocators as loc

class DeviceCategoryPage(BasePage):
    """
    仪器分类页面操作的封装
    """
    # i：输入框  bt：按钮  t：文本属性 p:弹窗提示
    t_devca_locator = (By.XPATH,'//span[contains(text(),"仪器分类")]')
    bt_add_devca_locator = (By.XPATH,'//span[contains(text(),"新增")]')
    i_devca_name_locator = (By.XPATH, '//*[@id="avue-view"]/div/div[2]/div/div[2]/div/form/div[2]/div[1]/div/div/div[1]/input')
    i_devca_sort_locator = (By.XPATH,'//*[@id="avue-view"]/div/div[2]/div/div[2]/div/form/div[2]/div[3]/div/div/div/div/input')
    bt_save_devca_locator = (By.XPATH,'//span[contains(text(),"保存")]')
    p_devca_locator = (By.XPATH,'//p[@class="el-message__content"]')
    i_select_devcaname_locator = (By.XPATH,'//input[@placeholder="请输入 分类名称"]')
    t_listone_devcaname_locator = (By.XPATH,'//span[@style="color: rgb(10, 103, 250); cursor: pointer;"]')
    bt_select_devca_locator = (By.XPATH,'//span[contains(text(),"搜索")]')
    bt_restting_devca_locator = (By.XPATH,'//span[contains(text(),"重置")]')
    bt_update_devca_locator = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/form/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/span[1]')
    t_text_devca_locator = (By.XPATH,'//textarea[@class="el-textarea__inner"]')
    bt_remove_devca_locator = (By.XPATH,'/html/body/div[1]/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div/form/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/span[2]')
    bt_remove_y_devca_locator = (By.XPATH,'//span[contains(text(),"确定")]')



    def get_device_category_index(self):
        """
        进入仪器分类页面
        :return:
        """
        # self.find(Device).click()
        # self.find(self.devc_locator).click()
        self.click(loc.t_device_ele)
        self.click(loc.t_devca_ele)
        return self

    def save_devicecategory(self,devca_name,devca_sort):
        """
        新增仪器分类并保存
        :param devca_name: 分类名称，必填项
        :param devca_sort: 分类排序，必填项
        :return:
        """
        self.click(loc.bt_add_devca_ele)
        self.send_value(loc.i_devca_name_ele,devca_name)
        self.send_value(loc.i_devca_sort_ele,devca_sort)
        self.click(loc.bt_save_devca_ele)
        save_devc_p = self.get_devca_p()
        return save_devc_p

    def select_devca(self,devcaname):
        """
        通过仪器分类名称查询仪器分类，并返回列表第一个仪器分类信息
        列表支持模糊匹配，通过部分关键词进行传参查询
        :param devicecategory: 仪器分类名称
        :return:
        """
        self.send_value(loc.i_select_devcaname_ele,devcaname)
        self.click(loc.bt_select_devca_ele)
        list_one_devcaname = self.find(loc.t_listone_devcaname_ele).text
        return list_one_devcaname

    def restting_devca(self):
        """
        搜索重置
        :return:
        """
        self.click(loc.bt_restting_devca_ele)
        return self

    def update_devca(self,devca_name,update_txt):
        """
        指定仪器分类基本信息编辑(编辑备注)
        :param devca_name: 仪器分类名称，查询条件，
        :param update_txt: 编辑内容
        :return:
        """
        self.select_devca(devca_name)
        self.click(loc.bt_update_devca_ele)
        self.send_value(loc.t_text_devca_ele,update_txt)
        self.click(loc.bt_save_devca_ele)
        update_devca_p = self.get_devca_p()
        self.restting_devca()
        return update_devca_p

    def remove_devca(self,devca_name):
        """
        指定仪器分类删除
        :param devca_name:仪器分类名称，查询条件
        :return:
        """
        self.select_devca(devca_name)
        self.click(loc.bt_remove_devca_ele)
        self.click(loc.bt_remove_y_devca_ele)
        remove_devca_p = self.get_devca_p()
        self.restting_devca()
        return remove_devca_p


    def get_devca_p(self):
        """
        获取操作完成后的弹窗提示
        :return:
        """
        devca_p = self.wait_element_visible(loc.p_devca_ele).text
        return devca_p

    def wati_invisibility(self):
        """
        等待页面操作完成的提示弹窗不可见
        :return:
        """
        wait = self.wati_element_invisibility(loc.p_devca_ele)
        return wait


