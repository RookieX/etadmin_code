# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

import sys


def build_cache_key(prefix, key_name=None):
    u'''
        cache_key生成器
    '''
    if not key_name:
        key_name = sys._getframe(1).f_code.co_name
    return '%s.%s' % (prefix, key_name)
