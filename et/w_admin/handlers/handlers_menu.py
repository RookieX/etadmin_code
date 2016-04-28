# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

import re

from et.common.routing import route
from et.common.extend.type_extend import null
from et.common.helper import ajax_helper

from et.bll.admin import MenuBLL
from et.model import Menu

from et.w_admin.common.base import AdminHandlerBase
from et.w_admin.common.helper import admin_helper


@route(r'/menu_list', r'/menu_list/(\d*)')
class MenuListHandler(AdminHandlerBase):
    def get(self, parent_id=0, page_index=1):
        parent_id = int(parent_id)
        page_index = int(page_index)

        menus = MenuBLL.query_by_parent_id(parent_id)

        # 构造返回上一级功能
        actual_path = re.sub(r'/\d*$', '', self.request.path)

        # 没有上一级，不需要返回功能
        if parent_id != 0:
            self.bag.back_url = '%s/%d' % (actual_path, menus[0].parent.parent.id)

        self.render('menu_list.html', menus)


@route(r'/menu_edit', r'/menu_edit/(\d+)')
class MenuEditHandler(AdminHandlerBase):
    def get(self, menu_id=0):
        menu_id = int(menu_id)

        menu = null

        if menu_id:
            menu = MenuBLL.query_by_id(menu_id)

            if not menu:
                return self.error(u'没有找到这个菜单')

        self.bag.parent_menus = null

        if menu:
            self.bag.parent_menus = MenuBLL.query_by_level(menu.level - 1)

        self.render('menu_edit.html', menu)

    def post(self, menu_id=0):
        arguments = self.get_arguments_dict(
            ['name',
             'display_name',
             'description',
             'level',
             'parent_menu',
             'url',
             'order'])

        arguments['id'] = menu_id

        if not arguments['name']:
            return ajax_helper.write_json(self, -1, u'请输入菜单名')

        if not arguments['display_name']:
            return ajax_helper.write_json(self, -2, u'请输入显示名')

        if not arguments['level']:
            return ajax_helper.write_json(self, -3, u'请输入级别')

        if arguments['level'] != '0' and not arguments['parent_menu']:
            return ajax_helper.write_json(self, -4, u'请选择父菜单')

        if not arguments['order']:
            return ajax_helper.write_json(self, -5, u'请输入排序')

        menu = Menu.build_from_dict(arguments)
        menu.parent = Menu.build_from_dict({'id': arguments['parent_menu']})

        if not menu_id:
            self.add(menu)
        else:
            self.update(menu)

    def add(self, menu):
        if MenuBLL.add(menu):
            return ajax_helper.write_json(self, 0)
        return ajax_helper.write_json(self, -1)

    def update(self, menu):
        if MenuBLL.update(menu):
            return ajax_helper.write_json(self, 0)
        return ajax_helper.write_json(self, -1)


@route(r'/load_menus')
class LoadMenusHandler(AdminHandlerBase):
    def get(self):
        level = self.get_argument('level', '')

        level = admin_helper.parse_int(level)

        if not level:
            return ajax_helper.write_json(self, -1, u'请先输入正确的level')

        menus = MenuBLL.query_by_level(level)

        ajax_helper.write_json(self, 0, data=[menu.to_dict() for menu in menus])
