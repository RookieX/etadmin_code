# -*- coding: utf-8 -*-
# Date: 16-2-10
# Author: 徐鹏程

u"""
    缓存帮助文件
"""

__admin_cache_prefix = 'w_admin'  # 后台管理系统缓存前缀
__admin_cache_version = 1  # 后台管理系统缓存版本号


def all_menu_cache_key():
    u"""
        全量菜单缓存键
    """
    return __build_cache_key(__admin_cache_prefix,
                             'all_menu',
                             __admin_cache_version)


def menu_cache_key_by_parent_id(parent_id):
    u"""
        根据父菜单缓存键

        :param parent_id: 父菜单id

        :type parent_id: long
    """
    return __build_cache_key(__admin_cache_prefix,
                             'menu',
                             __admin_cache_version,
                             'p/%d' % parent_id)


def admin_user_cache_key(user_name):
    u"""
        后台用户缓存键

        :param user_name: 用户名

        :type user_name: str
    """

    return __build_cache_key(__admin_cache_prefix,
                             'admin_user',
                             __admin_cache_version,
                             'user_name/%s' % user_name)


def __build_cache_key(prefix, key_name, version, subfix=None):
    u"""
        cache_key生成器

        :param prefix: 前缀
        :param key_name: 键名
        :param version: 版本号
        :param subfix: 后缀

        :type prefix: str
        :type key_name: str
        :type version: int
        :type subfix: str

        :rtype: str
        :return: cache key
    """

    if subfix:
        return '%s/%s/%s/%s' % (prefix, key_name, version, subfix)

    return '%s/%s/%s' % (prefix, key_name, version)
