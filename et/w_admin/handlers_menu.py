# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

import re

from et.common.routing import route

from et.bll.admin import MenuBLL

from et.w_admin.common.base import AdminHandlerBase


@route(r'/menu_list', r'/menu_list/(\d*)')
class MenuListHandler(AdminHandlerBase):
    def get(self, parent_id=0, page_index=1):
        parent_id = int(parent_id)
        page_index = int(page_index)

        self.bag.menus = MenuBLL.query_by_parent_id(parent_id)

        # 构造返回上一级功能
        actual_path = re.sub(r'/\d*$', '', self.request.path)

        # 没有上一级，不需要返回功能
        if parent_id != 0:
            self.bag.back_url = '%s/%d' % (actual_path, self.bag.menus[0].parent.parent.id)

        self.render('menu_list.html')


@route(r'/menu_edit', r'/menu_edit/(\d+)')
class MenuEditHandler(AdminHandlerBase):
    def get(self, menu_id=0):
        self.bag.menu = MenuBLL.query_by_id(menu_id)

        self.render('menu_edit.html')
