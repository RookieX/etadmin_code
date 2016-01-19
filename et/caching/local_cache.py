# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

from datetime import datetime, timedelta

from .cache_base import CacheBase


class LocalCache(CacheBase):
    u'''
        本地自定义缓存
    '''

    def __init__(self):
        super(LocalCache, self).__init__(None, None)

    def set(self, key, val, expire_seconds=None, expire_days=None):
        u'''
            写入缓存
            参数：
                key：键
                val：值
                expire_seconds：存活时间，单位--second
                expire_days：存活时间，单位--day

            存货时间优先取expire_seconds，默认为0，即永久缓存
        '''
        if expire_seconds:
            expires = expire_seconds
        elif expire_days:
            expires = expire_days * 24 * 60 * 60
        else:
            expires = 0

        self._client[key] = (val, datetime.now() + timedelta(seconds=expires))

    def get(self, key):
        u'''
            读取缓存
            参数:
                key：键
            返回值：缓存的值
        '''
        val, expires = self._client.get(key, (None, None))

        if val is None:
            return val

        # 过期处理
        if expires < datetime.now():
            self._client.pop(key, None)
            val = None

        return val

    def _create_client(self):
        return {}
