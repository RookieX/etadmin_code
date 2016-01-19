# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    后台相关基类
'''

from et.common.handler.session_handler import SessionHandler


class AdminHandlerBase(SessionHandler):
    u'''
        后台handler基类
    '''

    def check_auth(self, permission):
        u'''
            权限检查
            参数：
                permission：要检查的权限
        '''


def authentication(permission, fail):
    u'''
        权限认证装饰器
        参数：
            permission：要验证的权限
            fail：没有权限的处理
    '''

    def _wrapper(func):
        def __wrapper(*args, **kwargs):
            if _check_auth(permission, []):
                func(*args, **kwargs)
            else:
                fail(*args, **kwargs)

        return __wrapper

    return _wrapper


def _check_auth(permission, user_permissions):
    u'''
        验证用户权限
        参数：
            permission：要检查的权限
            user_permissions：用户的所有权限
    '''

    for perm in user_permissions:
        if perm == permission:
            return True

    return False
