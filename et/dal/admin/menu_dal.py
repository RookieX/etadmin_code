# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from ...sql_helper import mysql_helper
from ...model import Menu


class MenuDAL(object):
    @staticmethod
    def query_by_user_name(user_name):
        u"""
        根据用户名查找用户的菜单

        :param user_name: 用户名

        :type user_name: str

        :return: 菜单列表
        :rtype: list(Menu)
        """

        sql = u'''
            SELECT  id,
                    `name`,
                    display_name,
                    description,
                    `level`,
                    parent_id,
                    url,
                    `order`
            FROM menu AS m
            LEFT JOIN admin_user_menu_mapping AS map
            ON m.id = map.menu_id
            WHERE map.user_name = %s
        '''

        args = (user_name,)

        datas = mysql_helper.query(sql, args)

        return [Menu.build_from_dict(data) for data in datas]
