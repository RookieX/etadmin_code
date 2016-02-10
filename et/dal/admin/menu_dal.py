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
                    `order`,
                    create_datetime,
                    update_datetime
            FROM menu
            ORDER BY `order`
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
                    `order`,
                    create_datetime,
                    update_datetime
            FROM menu AS m
            LEFT JOIN admin_user_menu_mapping AS map
            ON m.id = map.menu_id
            WHERE map.user_name = %s
            ORDER BY `order`
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
                    `order`,
                    create_datetime,
                    update_datetime
            FROM menu
            WHERE parent_id = %s
            ORDER BY `order`
        '''

        args = (parent_id,)
        datas = mysql_helper.query(sql, args)

        return [_build_menu_item(data) for data in datas]

    @staticmethod
    def add(menu):
        u"""
            添加菜单

            :param menu: 要添加的菜单
            :type menu: Menu

            :rtype: bool
            :return: 是否成功
        """

        sql = u'''
            INSERT INTO menu
            (
              `name`,
              display_name,
              description,
              `level`,
              parent_id,
              url,
              `order`,
              create_datetime,
              update_datetime
            )
            VALUES
            (
              %s,%s,%s,%s,%s,%s,%s,%s,%s
            )
        '''
        args = (menu.name,
                menu.display_name,
                menu.description,
                menu.level,
                menu.parent.id,
                menu.url,
                menu.order,
                menu.create_datetime,
                menu.update_datetime
                )

        return mysql_helper.execute_non_query(sql, args)

    @staticmethod
    def update(menu):
        u"""
            更新菜单

            :param menu: 要更新的菜单
            :type menu: Menu

            :rtype: long
            :return: 受影响行数
        """
        sql = u'''
            UPDATE menu
            SET `name` = %s,
                display_name = %s,
                description = %s,
                `level` = %s,
                parent_id = %s,
                url = %s,
                `order` = %s,
                update_datetime = %s
            WHERE id = %s
        '''
        args = (menu.name,
                menu.display_name,
                menu.description,
                menu.level,
                menu.parent.id,
                menu.url,
                menu.order,
                menu.update_datetime,
                menu.id)

        return mysql_helper.execute_non_query(sql, args)


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
