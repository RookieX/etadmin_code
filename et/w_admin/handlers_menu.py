# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from et.common.routing import route

from et.bll.admin import MenuBLL

from et.w_admin.common.base import AdminHandlerBase


@route(r'/menu_list', r'/menu_list/(\d*)')
class MenuListHandler(AdminHandlerBase):
    def get(self, parent_id=0):
        parent_id = int(parent_id)
        self.bag.menus = MenuBLL.query_by_parent_id(parent_id)

        self.render('menu_list.html')
