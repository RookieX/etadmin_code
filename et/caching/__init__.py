# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

import sys

from ..common.helper import sys_path_extender

import config

sys_path_extender.extend(config.third_party_path)

from ali_memcached import AliMemcached
from local_cache import LocalCache
from local_memcached import LocalMemcached


def build_cache_key(prefix, key_name=None):
    u"""
        cache_key生成器

        :param prefix: 前缀
        :param key_name: 键名

        :type prefix: str
        :type key_name: str

        :rtype: str
        :return: cache key
    """
    if not key_name:
        key_name = sys._getframe(1).f_code.co_name
    return '%s.%s' % (prefix, key_name)
