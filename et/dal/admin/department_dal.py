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
                LEFT JOIN admin_user_department_mapping AS map
                ON map.department_id = dept.id
                WHERE map.user_name = %s
        '''

        args = (user_name,)

        data = mysql_helper.query_one(sql, args)

        dept = Department.build_from_dict(data)
        dept.default_top_menu = Menu.build_from_dict({'id': data['default_top_menu_id']})
        return dept