# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    session基类
"""

import uuid

from ...caching import LocalCache,LocalMemcached
from .base_handler import BaseHandler

cache = LocalMemcached()


class SessionHandler(BaseHandler):
    u"""
        带session功能的Handler
    """

    def __init__(self, application, request, **kwargs):
        self.cache = cache
        self.session_name = kwargs.get('session_name', 'SESSION')  # SESSION记录cookie的名称
        self.session_key = None  # cookie中记录的SESSION的key
        self.session_data = {}
        super(SessionHandler, self).__init__(application, request, **kwargs)

    def initialize(self):
        super(SessionHandler, self).initialize()
        self.session_key = self.get_secure_cookie(self.session_name)
        if self.session_key:
            self.session_data = self.cache.get(self.session_key)
            if self.session_data is None:
                self.session_data = {}

    def set_session(self, key, value):
        u"""
            设置session

            :param key: 键
            :param value: 值

            :type key: str
            :type value:
        """
        self.session_data[key] = value
        self._write_session_data()

    def get_session(self, key):
        u"""
            获取session

            :param key: 键

            :type key: str

            :rtype:
        """
        return self.session_data.get(key)

    def remove_session(self):
        u"""
            移除session
        """
        self.cache.remove(self.session_key)

    def _write_session_data(self):
        u"""
            记录session数据
        """

        if not self.session_key:
            self.session_key = str(uuid.uuid1())

        self.set_secure_cookie(self.session_name, self.session_key)
        self.cache.set(self.session_key, self.session_data, expire_seconds=1200)
