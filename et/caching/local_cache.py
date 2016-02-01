# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

import threading
from datetime import datetime, timedelta

from .cache_base import CacheBase


class LocalCache(CacheBase):
    u"""
        本地自定义缓存，单例实现
    """
    __mutex = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls.__mutex.acquire()
            if not hasattr(cls, '_instance'):
                cls._instance = super(LocalCache, cls).__new__(cls, *args, **kwargs)
            cls.__mutex.release()
        return cls._instance

    def __init__(self):
        super(LocalCache, self).__init__(None, None)

    def set(self, key, val, expire_seconds=None, expire_days=None):
        u"""
            写入缓存

            :param key: 键
            :param val: 值
            :param expire_seconds: 存活时间，单位--second
            :param expire_days: 存活时间，单位--day

            :type key: str
            :type val: object
            :type expire_seconds: int
            :type expire_days: int

            存货时间优先取expire_seconds，默认为0，即永久缓存
        """
        if expire_seconds:
            expires = expire_seconds
        elif expire_days:
            expires = expire_days * 24 * 60 * 60
        else:
            expires = None
        if expires:
            expire_time = datetime.now() + timedelta(seconds=expires)
        else:
            expire_time = 0

        self._client[key] = (val, expire_time)

    def get(self, key):
        u"""
            读取缓存

            :param key: 键

            :type key: str

            :return: 缓存的值
        """
        val, expires = self._client.get(key, (None, None))

        if val is None:
            return val

        if 0 == expires:
            return val

        # 过期处理
        if expires < datetime.now():
            self._client.pop(key, None)
            val = None

        return val

    def remove(self, key):
        u"""
            删除缓存

            :param key: 键

            :type key: str

            :return: 缓存的值
        """
        val, expires = self._client.pop(key, (None, None))

        if val is None:
            return val

        # 过期处理
        if expires < datetime.now():
            self._client.pop(key, None)
            val = None

        return val

    def _create_client(self):
        u"""
            创建缓存客户端
        """
        return {}
