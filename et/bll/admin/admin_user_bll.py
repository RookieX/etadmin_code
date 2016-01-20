# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ...common.helper import encrypt_helper
from ...caching import build_cache_key
from ...caching.local_cache import LocalCache

from ...dal.admin import AdminUserDAL

import config

cache = LocalCache()


class AdminUserBLL(object):
    @staticmethod
    def login(user_name, password):
        u'''
        登录

        :param user_name: 用户名
        :param password: 密码

        :rtype: bool
        :return: 登录是否成功
        '''

        pwd = encrypt_helper.password(password)

        return AdminUserDAL.login_exists(user_name, pwd)

    @staticmethod
    def query_by_user_name(user_name):
        u'''
        根据用户名查找用户信息

        :param user_name: 用户名
        :rtype: AdminUser
        :return: AdminUser，没有找到返回None
        '''
        cache_key = build_cache_key(config.cache_prefix)
        user = cache.get(cache_key)
        if not user:
            user = AdminUserDAL.query_by_user_name(user_name)
            if user:
                cache.set(cache_key, user, expire_seconds=config.default_cache_seconds)

        return user
