# -*- coding: utf-8 -*-
# Date: 16-1-8
# Author: 徐鹏程


class CacheBase(object):
    u"""
        缓存基类，提供通用的缓存操作方法
    """

    def __init__(self, host='127.0.0.1', port=11211):
        self.host = host
        self.port = port
        self._client = self._create_client()

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
            expires = 0

        self._client.set(key, val, time=expires)

    def get(self, key):
        u"""
            读取缓存

            :param key: 键

            :type key: str

            :return: 缓存的值
        """
        return self._client.get(key)

    def _create_client(self):
        u"""
            创建缓存客户端，由实际的缓存子类实现
        """
        return None
