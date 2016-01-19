# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    session基类
'''

from ...caching import local_cache

cache = local_cache.LocalCache()

from .base_handler import BaseHandler


class SessionHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(SessionHandler, self).__init__(application, request, **kwargs)
        self.cache = cache
