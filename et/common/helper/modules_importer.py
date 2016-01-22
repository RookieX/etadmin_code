# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    动态import模块
"""

import os
import imp
import re


def import_modules(path, pattern='.*\.py'):
    u"""
        动态导入module

        :param path: module路径
        :param pattern: 文件匹配正则表达式

        :type path: str
        :type pattern: str
    """

    def __iter_module(arg, dir_name, file_names):
        u"""
            遍历导入module

            :param arg: 额外参数
            :param dir_name: 目录名
            :param file_names: 文件名

            :type arg:
            :type dir_name: str
            :type file_names: list
        """
        for file_name in file_names:
            module_path = os.path.abspath(os.path.join(dir_name, file_name))
            if re.match(pattern, file_name):
                module_name = file_name.split('.')[0]
                imp.load_source(module_name, module_path)

    os.path.walk(path, __iter_module, None)
