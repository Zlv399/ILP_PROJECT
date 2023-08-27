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
from config.config import Device,TEST_HOST
from selenium.webdriver.common.by import By


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
    #//table/tbody/tr[1]/td[6]/div/span[1]
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
        self.click(Device)
        self.click(self.t_devca_locator)
        return self

    def save_devicecategory(self,devca_name,devca_sort):
        """
        新增仪器分类并保存
        :param devca_name: 分类名称，必填项
        :param devca_sort: 分类排序，必填项
        :return:
        """
        self.find(self.bt_add_devca_locator).click()
        self.send_value(self.i_devca_name_locator,devca_name)
        self.send_value(self.i_devca_sort_locator,devca_sort)
        self.click(self.bt_save_devca_locator)
        save_devc_p = self.get_devca_p()
        return save_devc_p

    def select_devca(self,devcaname):
        """
        通过仪器分类名称查询仪器分类，并返回列表第一个仪器分类信息
        列表支持模糊匹配，通过部分关键词进行传参查询
        :param devicecategory: 仪器分类名称
        :return:
        """
        self.send_value(self.i_select_devcaname_locator,devcaname)
        self.click(self.bt_select_devca_locator)
        list_one_devcaname = self.find(self.t_listone_devcaname_locator).text
        return list_one_devcaname

    def restting_devca(self):
        self.click(self.bt_restting_devca_locator)
        return self

    def update_devca(self,devca):
        """
        仪器分类基本信息编辑(编辑备注)
        :param devca: 编辑修改仪器分类的内容1
        :return:
        """
        #self.driver.find_elements(*self.bt_update_devca_locator)[1].click()
        self.click(self.bt_update_devca_locator)
        self.send_value(self.t_text_devca_locator,devca)
        self.click(self.bt_save_devca_locator)
        update_devca_p = self.get_devca_p()
        return update_devca_p

    def remove_devca(self):
        self.click(self.bt_remove_devca_locator)
        self.click(self.bt_remove_y_devca_locator)
        remove_devca_p = self.get_devca_p()
        return remove_devca_p


    def get_devca_p(self):
        """
        获取操作完成后的弹窗提示
        :return:
        """
        devca_p = self.wait_element_visible(self.p_devca_locator).text
        return devca_p


