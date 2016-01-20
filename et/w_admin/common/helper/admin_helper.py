# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    后台通用方法
'''

import uuid

from et.w_admin import config


def set_user_session(handler, user_info):
    u'''
        设置用户信息session
    '''

    session_key = str(uuid.uuid1())

    handler.set_cookie(config.session_cookie_key, session_key)
    handler.cache.set(session_key, user_info, expire_seconds=1200)


def get_user_info_from_session(handler, key):
    u'''
        从缓存中获取用户信息
    '''
    return handler.cache.get(key)
