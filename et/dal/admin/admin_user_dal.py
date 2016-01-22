# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ...sql_helper import mysql_helper
from ...model import AdminUser


class AdminUserDAL(object):
    @staticmethod
    def login_exists(user_name, pwd):
        u"""
        用登录信息判断用户是否存在

        :param user_name: 用户名
        :param pwd: 密码

        :type user_name: str
        :type pwd: str

        :rtype: bool
        :return: 是否存在
        """

        sql = u'''
            SELECT COUNT(*) FROM admin_user
            WHERE user_name = %s AND `password` = %s
        '''

        args = (user_name, pwd)

        return mysql_helper.query_scalar(sql, args) == 1

    @staticmethod
    def query_by_user_name(user_name):
        u"""
        根据用户名查找用户信息

        :param user_name: 用户名
        :type user_name: str

        :rtype: AdminUser
        :return: AdminUser，没有找到返回None
        """

        sql = u'''
                SELECT  user_name,
                        display_name,
                        password,
                        user_type_id,
                        create_datetime,
                        update_datetime,
                        department_id,
                        position_id,
                        parent_position_id
            FROM admin_user
            WHERE user_name = %s
        '''
        args = (user_name,)

        user = mysql_helper.query_one(sql, args)

        if user:
            return AdminUser.build_from_dict(user)
