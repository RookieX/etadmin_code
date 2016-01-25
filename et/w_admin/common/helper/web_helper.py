# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    后台通用方法
"""

from et.w_admin import config


def set_login_session(handler, user_info):
    u"""
        设置用户登录信息session

        :param handler: BaseHandler
        :param user_info: 用户信息

        :type handler: BaseHandler
        :type user_info: AdminUser
    """
    handler.set_session(config.login_session_key, user_info)


def get_login_session(handler):
    u"""
        从session中获取用户登录信息

        :param handler: BaseHandler

        :type handler: BaseHandler

        :return: session信息
    """
    return handler.get_session(config.login_session_key)


def has_sub_menus(handler, menu_id):
    u"""
        判断某个菜单是否有子菜单

        :param menu_id: 菜单id
        :param handler: BaseHandler

        :type menu_id: int
        :type handler: BaseHandler

        :rtype: bool

        :return: 返回是否存在
    """

    user_info = get_login_session(handler)

    if not user_info:
        return False

    for menu in user_info.menus:
        if menu.parent.id == menu_id:
            return True

    return False
