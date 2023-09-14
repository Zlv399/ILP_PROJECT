"""
-- coding: utf-8 --
@project:ILP_PROJECT
@File:device_data.py
@IDE:PyCharm
@Author:fangyx
@Date:2023/8/17 22:21
"""

import time

device_category = [
    {'devca_name':'自动化测试分类{}'.format(time.strftime('%y%m%d-%H:%M:%S')),
     'sort':'0',
     'expected':'操作成功!'
     }
]
select_device_category = [
    {'select_devca':'自动化测试分类'}
]
update_device_category = [
    {   'select_devca':'自动化测试分类',
        'update_devca_text':'UI自动化编辑仪器分类备注信息{}'.format(time.strftime('%y%m%d-%H:%M:%S')),
        'expected':'操作成功!'
        }
]

