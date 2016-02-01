# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from ...common.extend.type_extend import null
from ...dal.admin import MenuDAL
from ...model import Menu
from ...caching import LocalCache, build_cache_key

import config

cache = LocalCache()


class MenuBLL(object):
    @staticmethod
    def query_all():
        u"""
            查找所有菜单

            :rtype: list[Menu]
        """

        cache_key = build_cache_key(config.cache_prefix)
        menus = cache.get(cache_key)

        if not menus:
            menus = MenuDAL.query_all()
            _build_menu_hierarchy(menus)
            cache.set(cache_key, menus)

        return menus

    @classmethod
    def query_by_parent_id(cls, parent_id):
        u"""
            根据parent_id查找子菜单

            :param parent_id: 父菜单id
            :type parent_id: int

            :rtype: list[Menu]
            :return: 菜单列表
        """
        cache_key = build_cache_key(config.cache_prefix, str(parent_id))
        menus = cache.get(cache_key)
        if not menus:
            menus = filter(lambda m: m.parent.id == parent_id, cls.query_all())
            # menus = [_format_menu_item(menu) for menu in menus]
            cache.set(cache_key, menus)

        return menus

    @classmethod
    def query_by_id(cls, menu_id):
        u"""
            根据id查询菜单

            :param menu_id: 菜单id

            :type menu_id: long

            :rtype: Menu
            :return: id对应的菜单
        """

        menus = filter(lambda m: m.id == menu_id, cls.query_all())
        if menus:
            return menus[0]

        return None

    @classmethod
    def query_by_level(cls, level):
        u"""
            根据level查询菜单

            :param level: 菜单level

            :type level: int

            :rtype: list[Menu]
            :return: level对应的菜单
        """
        menus = filter(lambda m: m.level == level, cls.query_all())
        return menus


def _build_menu_hierarchy(menus):
    u"""
        构造菜单层级

        :param menus: 菜单列表
        
        :type menus: list[Menu]

        :rtype: list[Menu]
    """

    for menu in menus:
        menu_id = menu.id

        for sub_menu in menus:
            if sub_menu.parent.id == menu_id:
                sub_menu.parent = menu
                menu.sub_menus.add(sub_menu)

    return menus
