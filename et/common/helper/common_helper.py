# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程
u"""
    通用方法
"""
import uuid
import re


def UUID():
    u"""
        生成uuid字符串

        :rtype: str
        :return: uuid字符串
    """

    uuid_str = str(uuid.uuid1())
    return re.sub('-', '', uuid_str)
