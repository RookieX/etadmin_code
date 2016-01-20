# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

import uuid
import re


def UUID():
    u'''
        生成uuid字符串
    '''

    uuid_str = str(uuid.uuid1())
    return re.sub('-', '', uuid_str)
