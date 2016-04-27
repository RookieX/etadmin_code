# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    后台相关基类
"""

from et.common.handler import SessionHandler
from et.w_admin.common import common_response
from et.w_admin.common.helper import web_helper


class AdminHandlerBase(SessionHandler):
    u"""
        后台handler基类
    """

    def __init__(self, *args, **kwargs):
        super(AdminHandlerBase, self).__init__(*args, **kwargs)

    def check_auth(self, permission):
        u"""
            权限检查

            :param permission: 要检查的权限
            :type permission: str

            :rtype: bool
            :return: 检查结果
        """
        user = web_helper.get_login_session(self)
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
            super(AdminHandlerBase, self).write_error(status_code, **kwargs)


def authentication(permission, no_perm_callback, fail_callback):
    u"""
        权限认证装饰器

        :param permission: 要验证的权限
        :param no_perm_callback:没有权限的回调
        :param fail_callback: 无法获取权限回调

        :type permission: str
        :type no_perm_callback: function
        :type fail_callback: function
    """

    def _wrapper(func):
        def __wrapper(handler, *args, **kwargs):
            user = web_helper.get_login_session(handler)
            if not user:
                return fail_callback(handler, *args, **kwargs)
            if _check_auth(permission, user.permissions):
                return func(handler, *args, **kwargs)
            else:
                return no_perm_callback(handler, *args, **kwargs)

        return __wrapper

    return _wrapper


def login(func):
    u"""
        普通登录验证装饰器
    """

    def _wrapper(handler, *args, **kwargs):
        return __login(func, handler, 'html', *args, **kwargs)

    return _wrapper


def json_login(func):
    u"""
        json登录验证装饰器
    """

    def _wrapper(handler, *args, **kwargs):
        return __login(func, handler, 'json', *args, **kwargs)

    return _wrapper


def __login(func, handler, resp_type, *args, **kwargs):
    u"""
        登录验证
    """
    user = web_helper.get_login_session(handler)
    if user:
        return func(handler, *args, **kwargs)
    else:
        if resp_type == 'json':
            return common_response.resp_need_login_json(handler, *args, **kwargs)
        else:
            return common_response.resp_need_login_regular(handler, *args, **kwargs)


def _check_auth(permission, user_permissions):
    u"""
        验证用户权限

        :param permission: 要检查的权限
        :param user_permissions: 用户的所有权限

        :type permission: str
        :type user_permissions: list

        :rtype: bool
        :return: 验证结果
    """

    for perm in user_permissions:
        if perm.name == permission:
            return True

    return False
