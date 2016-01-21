# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    后台通用方法
'''

from et.w_admin import config


def set_login_session(handler, user_info):
    u'''
        设置用户登录信息session
    '''
    handler.set_session(config.login_session_key, user_info)


def get_login_session(handler):
    u'''
        从session中获取用户登录信息
    '''
    return handler.get_session(config.login_session_key)
