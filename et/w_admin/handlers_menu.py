# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from et.common.routing import route

from et.bll.admin import MenuBLL

from et.w_admin.common.base import AdminHandlerBase


@route(r'/menu_list')
class MenuListHandler(AdminHandlerBase):
    def get(self):
        self.bag.menus = MenuBLL.query_all()

        self.render('menu_list.html')
