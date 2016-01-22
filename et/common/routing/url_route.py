# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    路由相关类
"""


class __UrlRoute(object):
    u"""
        Url路由
    """
    __routes = {}

    def __init__(self, url_pattern):
        self.pattern = url_pattern

    def __call__(self, request):
        self.__routes[self.pattern] = request
        return request

    @classmethod
    def routes(cls):
        u"""
            返回路由表
            
            :return: 路由表
        """
        return [(k, v) for k, v in cls.__routes.items()]


route = __UrlRoute
