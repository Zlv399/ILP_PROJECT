"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:device_category_loc.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/9/6 0:02
"""

from selenium.webdriver.common.by import By

class DeviceCategoryLocators:
    """
    1、仪器管理菜单
    2、仪器分类菜单
    3、新增分类按钮
    4、分类名称输入框
    5、分类排序输入框
    6、新增、编辑分类保存按钮
    7、页面弹窗提示
    8、列表查询输入框
    9、列表第一个分类名称
    10、列表查询按钮
    11、列表重置按钮
    12、列表第一个分类编辑按钮
    13、分类备注信息
    14、列表第一个分类删除按钮
    15、删除二次确认
    """
    # i：输入框  bt：按钮  t：文本属性 p:弹窗提示
    t_device_ele = (By.XPATH,'//span[contains(text(),"仪器管理")]')
    t_devca_ele = (By.XPATH,'//span[contains(text(),"仪器分类")]')
    bt_add_devca_ele = (By.XPATH,'//span[contains(text(),"新增")]')
    i_devca_name_ele = (By.XPATH, '//input[@type="text"][@class="el-input__inner"][@maxlength="50"]')
    i_devca_sort_ele = (By.XPATH,'//input[@type="text"][@min="1"]')
    bt_save_devca_ele = (By.XPATH,'//span[contains(text(),"保存")]')
    p_devca_ele = (By.XPATH,'//p[@class="el-message__content"]')
    i_select_devcaname_ele = (By.XPATH,'//input[@placeholder="请输入 分类名称"]')
    t_listone_devcaname_ele = (By.XPATH,'//span[@style="color: rgb(10, 103, 250); cursor: pointer;"]')
    bt_select_devca_ele = (By.XPATH,'//span[contains(text(),"搜索")]')
    bt_restting_devca_ele = (By.XPATH,'//span[contains(text(),"重置")]')
    bt_update_devca_ele = (By.XPATH,'//*[@id="avue-view"]/div/div/div/div[2]/div/form/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/span[1]')
    t_text_devca_ele = (By.XPATH,'//textarea[@class="el-textarea__inner"]')
    bt_remove_devca_ele = (By.XPATH,'//*[@id="avue-view"]/div/div/div/div[2]/div/form/div/div[4]/div[2]/table/tbody/tr[1]/td[6]/div/span[2]')
    bt_remove_y_devca_ele = (By.XPATH,'//span[contains(text(),"确定")]')