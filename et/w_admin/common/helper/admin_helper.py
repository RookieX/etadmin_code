# -*- coding: utf-8 -*-
# Date: 16-4-9
# Author: 徐鹏程

u"""
    后台系统相关的帮助方法
"""

import re


def parse_int(s):
    u"""
        将字符串解析为整数
        如果字符串不是一个整数，返回None

        :param s: 整数字符串
        :type s: str

        :return: 解析结果
        :rtype: int | None
    """

    re_pattern = r'^-?\d+$'
    if not re.match(re_pattern, s):
        return None
    return int(s)
