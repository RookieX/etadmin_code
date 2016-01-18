# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程

u'''
    扩展sys.path，导入第三方包的功能
'''

import sys
import os
import re


def extend(extend_path, pattern='.*\.egg$'):
    u'''
        扩展sys.path
        参数：
            extend_path：第三方包所在路径
            pattern：搜索第三方包的正则表达式字符串
    '''

    def __visit(arg, dir_name, file_names):
        u'''
            遍历文件路径，扩展sys.path
        '''
        for file_name in file_names:
            if re.match(pattern, file_name):
                egg_path = os.path.join(dir_name, file_name)
                if egg_path not in sys.path:
                    sys.path.append(egg_path)

    os.path.walk(extend_path, __visit, None)
