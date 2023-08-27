"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:config.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/13 22:39
"""

import os
from selenium.webdriver.common.by import By

# 隐式等待时间
IMPLICTLY_WAIT_TIMEOUT = 20

# host
TEST_HOST = "http://192.168.32.70:2888/"
UAT_HOST = "http://192.168.32.70:2888/"

# 获取项目根目录（获取当前文件父级目录的上一级目录）
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告地址
REPORTS_PATH = os.path.join(ROOT_PATH, "reports")

# image_path 保存截图的路径
IMAGE_PATH = os.path.join(REPORTS_PATH, "screeshots")

# 用于文件上传功能的文件地址
FILES_PATH = os.path.join(ROOT_PATH, "files")

#模块父级菜单元素定位
Device  = (By.XPATH,'//span[contains(text(),"仪器管理")]')