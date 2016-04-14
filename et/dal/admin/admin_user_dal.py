# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ...common.extend.type_extend import null

from ...sql_helper import mysql_helper
from ...model import AdminUser
from ...model import Department
from ...model import Position
from ...model import Menu


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
            SELECT  admin.user_name,
                    admin.display_name,
                    admin.password,
                    admin.user_type_id,
                    admin.create_datetime,
                    admin.update_datetime,
                    admin.position_id,
                    admin.department_id,
                    pos.name AS pos_name,
                    pos.parent_position_id AS ppos_id,
                    dept.name AS dept_name,
                    dept.default_top_menu_id
            FROM admin_user AS admin
            LEFT JOIN position AS pos
            ON admin.position_id = pos.id
            LEFT JOIN department AS dept
            ON admin.department_id = dept.id
            WHERE admin.user_name = %s
        '''
        args = (user_name,)

        data = mysql_helper.query_one(sql, args)

        if data:
            return _build_admin_user(data)

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
            SELECT  admin.user_name,
                    admin.display_name,
                    admin.password,
                    admin.user_type_id,
                    admin.create_datetime,
                    admin.update_datetime,
                    admin.position_id,
                    admin.department_id,
                    pos.name AS pos_name,
                    pos.parent_position_id AS ppos_id,
                    dept.name AS dept_name
            FROM admin_user AS admin
            LEFT JOIN position AS pos
            ON admin.position_id = pos.id
            LEFT JOIN department AS dept
            ON admin.department_id = dept.id
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
    admin_user.department = Department.build_from_dict(
        {'id': data.get('department_id', null), 'name': data.get('dept_name', null)})
    admin_user.department.default_top_menu = Menu.build_from_dict({'id': data.get('default_top_menu_id', null)})
    admin_user.position = Position.build_from_dict(
        {'id': data.get('position_id', null), 'name': data.get('pos_name', null)})
    admin_user.position.parent_position = Position.build_from_dict({'id': data.get('ppos_id', null)})

    return admin_user
