"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:1233.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/15 23:23
"""

from selenium import webdriver
from datetime import datetime
import os
from config.config import IMAGE_PATH

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
ts_str = datetime.now().strftime("%y-%m_%d-%H-%M-%S")
file_name = os.path.join(IMAGE_PATH, ts_str) + '.png'
print(file_name)
driver.save_screenshot(file_name)