# -*- coding: utf-8 -*-
# Date: 16-1-8
# Author: 徐鹏程

import bmemcached

from cache_base import CacheBase

host = '127.0.0.1'
port = 11211


class LocalMemcached(CacheBase):
    u"""
        本地memcached缓存
    """

    def __init__(self):
        super(LocalMemcached, self).__init__(host, port)

    def _create_client(self):
        u"""
            创建缓存客户端
        """
        return bmemcached.Client(('%s:%s' % (host, port)))
