# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from datetime import datetime

from ...common.helper import encrypt_helper, cache_helper
from ...caching.local_cache import LocalCache

from ...dal.admin import AdminUserDAL
from ...dal.admin import PermissionDAL
from ...dal.admin import MenuDAL
from ...dal.admin import DepartmentDAL
from ...dal.admin import PositionDAL

from ...model import AdminUser
from ...model import Department

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
        if user:
            user.permissions = PermissionDAL.query_by_user_name(user_name)
            user.menus = MenuDAL.query_by_user_name(user_name)

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

    @staticmethod
    def add(admin_user):
        u'''
            添加后台用户

            :param admin_user: 后台用户
            :type admin_user: AdminUser

            :return: 添加是否成功
            :rtype: bool
        '''

        admin_user.create_datetime = admin_user.update_datetime = datetime.now()

        # 补全职位信息
        position = PositionDAL.query_by_id(admin_user.position.id)

        admin_user.department = Department.build_from_dict({'id': position.department.id})
        return AdminUserDAL.add(admin_user) == 1

    @staticmethod
    def update(admin_user):
        u'''
            更新后台用户

            :param admin_user: 后台用户
            :type admin_user: AdminUser

            :return: 更新是否成功
            :rtype: bool
        '''

        admin_user.update_datetime = datetime.now()

        return AdminUserDAL.update(admin_user) == 1
