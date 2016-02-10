# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ...common.helper import encrypt_helper, cache_helper
from ...caching.local_cache import LocalCache

from ...dal.admin import AdminUserDAL
from ...dal.admin import PermissionDAL
from ...dal.admin import MenuDAL
from ...dal.admin import DepartmentDAL

from ..common.helper import page_helper
import config

cache = LocalCache()


class AdminUserBLL(object):
    @staticmethod
    def login(user_name, password):
        u"""
        登录验证

        :param user_name: 用户名
        :param password: 密码

        :type user_name: str
        :type password: str

        :rtype: bool
        :return: 登录是否成功
        """
        pwd = encrypt_helper.password(password)

        return AdminUserDAL.login_exists(user_name, pwd)

    @staticmethod
    def query_full_by_user_name(user_name):
        u"""
        根据用户名查找用户信息，包括基本信息，菜单和权限

        :param user_name: 用户名

        :type user_name: str

        :rtype: AdminUser
        :return: AdminUser，没有找到返回None
        """

        user = AdminUserDAL.query_by_user_name(user_name)
        user.permissions = PermissionDAL.query_by_user_name(user_name)
        user.menus = MenuDAL.query_by_user_name(user_name)
        user.department = DepartmentDAL.query_by_user_name(user_name)

        return user

    @staticmethod
    def query(page_index, page_size):
        u"""
            分页查找后台用户

            :param page_index: 页号
            :param page_size:  分页大小

            :type page_index: int
            :type page_size:  int

            :rtype: list[AdminUser]
            :return: 后台用户列表
        """
        start, end = page_helper.calc_page_range(page_index, page_size)
        return AdminUserDAL.query(start, end)
