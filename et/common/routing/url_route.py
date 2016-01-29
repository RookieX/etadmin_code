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

    def __init__(self, *args):
        self.patterns = args

    def __call__(self, request):
        for pattern in self.patterns:
            self.__routes[pattern] = request
        return request

    @classmethod
    def routes(cls):
        u"""
            返回路由表
            
            :return: 路由表
        """
        return [(k, v) for k, v in cls.__routes.items()]


route = __UrlRoute
