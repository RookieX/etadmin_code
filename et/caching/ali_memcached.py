# -*- coding: utf-8 -*-
# Date: 16-1-7
# Author: 徐鹏程

import bmemcached

from .cache_base import CacheBase

host = '4fc7a837292a4b42.m.cnbjalinu16pub001.ocs.aliyuncs.com'
port = 11211
user = '4fc7a837292a4b42'
pwd = 'cacheET2015'


class AliMemcached(CacheBase):
    u"""
        阿里云memcached缓存
    """

    def __init__(self):
        super(AliMemcached, self).__init__(host, port)

    def _create_client(self):
        u"""
            创建缓存客户端
        """
        return bmemcached.Client(('%s:%s' % (host, port)), user, pwd)
