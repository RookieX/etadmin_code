# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from ...sql_helper import mysql_helper
from ...model import Department
from ...model import Menu


class DepartmentDAL(object):
    @staticmethod
    def query_by_user_name(user_name):
        u"""
            根据用户名查找用户的部门

            :param user_name: 用户名
            :type user_name: str

            :rtype: Department
            :return: 部门
        """

        sql = u'''
                SELECT  id,
                        dept.name,
                        default_top_menu_id
                FROM department AS dept
                LEFT JOIN admin_user AS admin
                ON admin.department_id = dept.id
                WHERE admin.user_name = %s
        '''

        args = (user_name,)

        data = mysql_helper.query_one(sql, args)

        if data:
            dept = Department.build_from_dict(data)
            dept.default_top_menu = Menu.build_from_dict({'id': data['default_top_menu_id']})
            return dept

        return None

    @staticmethod
    def query(start, end):
        u"""
            分页查找部门

            :param start: 开始记录
            :param end:  结束记录

            :type start: int
            :type end:  int

            :rtype: list[Department]
            :return: 部门列表
        """

        sql = u'''
                SELECT  dept.id,
                        dept.name,
                        default_top_menu_id,
                        menu.name AS menu_name,
                        dept.create_datetime,
                        dept.update_datetime
                FROM department AS dept
                LEFT JOIN menu
                ON dept.default_top_menu_id = menu.id
                LIMIT %s,%s;
        '''

        args = (start - 1, end - start)

        datas = mysql_helper.query(sql, args)

        return [_build_department(data) for data in datas]

    @staticmethod
    def find_by_id(dept_id):
        u"""
            根据部门id查找部门信息

            :param dept_id: 部门id
            :type dept_id: int

            :return: 部门信息
            :rtype: Department
        """
        sql = u'''
                SELECT id,
                        `name`,
                        default_top_menu_id,
                        create_datetime,
                        update_datetime
                FROM department
                WHERE id = %s;
        '''

        args = (dept_id,)
        data = mysql_helper.query_one(sql, args)

        return _build_department(data)

    @staticmethod
    def add(dept):
        u"""
            新增部门

            :param dept: 部门
            :type dept: Department

            :return: 受影响行数
            :rtype: int
        """
        sql = u'''
            INSERT INTO department
            (
              `name`,
              default_top_menu_id,
              create_datetime,
              update_datetime
            )
            VALUES
            (%s,%s,%s,%s)
        '''

        args = (dept.name, dept.default_top_menu.id, dept.create_datetime, dept.update_datetime)

        return mysql_helper.execute_non_query(sql, args)

    @staticmethod
    def update(dept):
        u"""
            更新部门

            :param dept: 部门
            :type dept: Department

            :return: 受影响行数
            :rtype: int
        """
        sql = u'''
            UPDATE department
            SET `name`=%s,
                default_top_menu_id=%s,
                update_datetime=%s
            WHERE id=%s
        '''
        args = (dept.name, dept.default_top_menu.id, dept.update_datetime, dept.id)
        result = mysql_helper.execute_non_query(sql, args)
        return result


def _build_department(data):
    u"""
        构造部门信息

        :param data: 部门信息

        :type data: dict

        :rtype: Department
        :return: 部门
    """

    dept = Department.build_from_dict(data)
    dept.default_top_menu = Menu.build_from_dict({'id': data['default_top_menu_id'], 'name': data.get('menu_name')})

    return dept
