# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ...sql_helper import mysql_helper
from ...model import AdminUser  # , UserType, Department, Position


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
                        position_id
            FROM admin_user
            WHERE user_name = %s
        '''
        args = (user_name,)

        user = mysql_helper.query_one(sql, args)

        if user:
            return AdminUser.build_from_dict(user)

    @staticmethod
    def query(start, end):
        u"""
            分页查找后台用户

            :param start: 开始记录
            :param end:  结束记录

            :type start: int
            :type end:  int

            :rtype: list[AdminUser]
            :return: 后台用户列表
        """

        sql = u'''
            SELECT  user_name,
                    display_name,
                    password,
                    user_type_id,
                    create_datetime,
                    update_datetime,
                    position_id
            FROM admin_user
            LIMIT %s,%s
        '''

        args = (start - 1, end - start)

        datas = mysql_helper.query(sql, args)

        return [_build_admin_user(data) for data in datas]


def _build_admin_user(data):
    u"""
        构造后台用户信息

        :param data: 后台用户信息

        :type data: dict

        :rtype: AdminUser
        :return: 后台用户
    """
    admin_user = AdminUser.build_from_dict(data)
    admin_user.user_type = UserType.build_from_dict()
    admin_user.department = Department.build_from_dict()
    admin_user.position = Position.build_from_dict()
    admin_user.parent_position = Position.build_from_dict()

    return admin_user
