# -*- coding: utf-8 -*-
# Date: 16-1-8
# Author: 徐鹏程

import bmemcached

host = '127.0.0.1'
port = 11211

from cache_base import CacheBase


class LocalMemcached(CacheBase):
    u'''
        本地memcached缓存
    '''
    def __init__(self):
        super(self.__class__, self).__init__(host, port)

    def _create_client(self):
        return bmemcached.Client(('%s:%s' % (host, port)))
