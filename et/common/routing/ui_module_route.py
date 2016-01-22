# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程
u"""
    注册UIModule相关类
"""


class __UIModule(object):
    u"""
        注册UIModule
    """
    __modules = {}

    def __init__(self, url_pattern):
        self.pattern = url_pattern

    def __call__(self, request):
        self.__modules[self.pattern] = request
        return request

    @classmethod
    def moules(cls):
        u"""
            返回UIModules列表

            :return: UIModules列表
        """
        return {k: v for k, v in cls.__modules.items()}


UIModule = __UIModule
