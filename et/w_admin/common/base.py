# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    后台相关基类
'''

from et.common.extend.type_extend import dynamic
from et.common.handler.session_handler import SessionHandler

from et.w_admin.common.helper import admin_helper


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
        user = admin_helper.get_login_session(self)
        if not user:
            return False

        return _check_auth(permission, user.permissions)

    def write_error(self, status_code=500, **kwargs):
        if status_code == 404:
            self.write(u'页面找不到')
        elif status_code == 400:
            self.write(u'请求缺少参数')
        elif status_code == 500:
            self.write(u'服务器出错')
        else:
            super(AdminHandlerBase, self).send_error(status_code, **kwargs)


def authentication(permission, no_perm_callback, fail_callback):
    u'''
        权限认证装饰器
        参数：
            permission：要验证的权限
            no_perm_callback：没有权限的处理
            fail_callback：无法获取权限处理
    '''

    def _wrapper(func):
        def __wrapper(handler, *args, **kwargs):
            user = admin_helper.get_login_session(handler)
            if not user:
                return fail_callback(handler, *args, **kwargs)
            if _check_auth(permission, user.permissions):
                return func(handler, *args, **kwargs)
            else:
                return no_perm_callback(handler, *args, **kwargs)

        return __wrapper

    return _wrapper


def login(fail):
    u'''
        登录验证装饰器
    '''

    def _wrapper(func):
        def __wrapper(handler, *args, **kwargs):
            user = admin_helper.get_login_session(handler)
            if user:
                return func(handler, *args, **kwargs)
            else:
                return fail(handler, *args, **kwargs)

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
        if perm.name == permission:
            return True

    return False
