# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from ...dal.admin import MenuDAL


class MenuBLL(object):
    @staticmethod
    def query_all():
        u"""
            查找所有菜单
        """
        menus = MenuDAL.query_all()

        for menu in menus:
            menu_id = menu.id

            for sub_menu in filter(lambda m: m.parent.id == menu_id, menus):
                sub_menu.parent = menu

        return menus
