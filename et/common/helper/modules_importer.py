# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    动态import模块
'''

import os
import imp
import re


def import_modules(path, pattern='.*\.py'):
    u'''
        动态导入module
        参数:
            path：module路径
            pattern：文件匹配正则表达式
    '''

    def __iter_module(arg, dir_name, file_names):
        for file_name in file_names:
            module_path = os.path.abspath(os.path.join(dir_name, file_name))
            if re.match(pattern, file_name):
                module_name = file_name.split('.')[0]
                imp.load_source(module_name, module_path)

    os.path.walk(path, __iter_module, None)
