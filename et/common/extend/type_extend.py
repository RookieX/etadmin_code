# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    类型扩展
'''


class Null(object):
    u'''
        空类型，无任何实际属性
    '''

    def __str__(self):
        return ''

    def __getattr__(self, item):
        return self

    def __getattribute__(self, item):
        return self

    def __eq__(self, other):
        if other is None:
            return True

        if other is Null:
            return True

        if other == '':
            return True

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return False


class Dynamic(object):
    u'''
        动态类型，可添加任意属性。
        访问不存在的属性返回Null实例。
    '''

    def __setattr__(self, key, value):
        super(Dynamic, self).__setattr__(key, value)

    def __getattr__(self, item):
        return null

    def __setitem__(self, key, value):
        super(Dynamic, self).__setattr__(key, value)

    def __getitem__(self, item):
        return super(Dynamic, self).__getattribute__(item)


null = Null()
dynamic = Dynamic
