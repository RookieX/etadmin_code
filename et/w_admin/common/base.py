# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    后台相关基类
'''

from et.common.extend.type_extend import dynamic
from et.common.handler.session_handler import SessionHandler


class AdminHandlerBase(SessionHandler):
    u'''
        后台handler基类
    '''

    def __init__(self, *args, **kwargs):
        super(AdminHandlerBase, self).__init__(*args, **kwargs)

        self.bag = dynamic()

    def render(self, template_name):
        super(AdminHandlerBase, self).render(template_name, bag=self.bag)

    def check_auth(self, permission):
        u'''
            权限检查
            参数：
                permission：要检查的权限
        '''

    def write_error(self, status_code=500, **kwargs):
        if status_code == 404:
            self.write(u'页面找不到')
        elif status_code == 400:
            self.write(u'请求缺少参数')
        elif status_code == 500:
            self.write(u'服务器出错')
        else:
            super(AdminHandlerBase, self).send_error(status_code, **kwargs)


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


def login(fail):
    u'''
        登录验证装饰器
    '''

    def _wrapper(func):
        def __wrapper(self,*args, **kwargs):
            session_key = self.get

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
