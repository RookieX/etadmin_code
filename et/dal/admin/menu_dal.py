# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from ...sql_helper import mysql_helper
from ...model import Menu


class MenuDAL(object):
    @staticmethod
    def query_all():
        u"""
            查找所有菜单
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
            FROM menu
        '''

        datas = mysql_helper.query(sql)

        return [_build_menu_item(data) for data in datas]

    @staticmethod
    def query_by_user_name(user_name):
        u"""
        根据用户名查找用户的菜单

        :param user_name: 用户名

        :type user_name: str

        :return: 菜单列表
        :rtype: list[Menu]
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

        return [_build_menu_item(data) for data in datas]

    @staticmethod
    def query_by_parent_id(parent_id):
        u"""
            根据parent_id查找子菜单

            :param parent_id: 父菜单id
            :type parent_id: int

            :rtype: list[Menu]
            :return: 菜单列表
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
            FROM menu
            WHERE parent_id = %s
        '''

        args = (parent_id,)
        datas = mysql_helper.query(sql, args)

        return [_build_menu_item(data) for data in datas]


def _build_menu_item(data):
    u"""
        构造菜单项

        :param data: 源数据

        :type data: dict

        :rtype: Menu
    """

    menu = Menu.build_from_dict(data)

    menu.parent = Menu.build_from_dict({'id': data['parent_id']})

    return menu
