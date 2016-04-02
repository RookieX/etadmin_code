# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程

from et.bll.admin import AdminUserBLL
from et.common.routing.url_route import route
from et.w_admin import config
from et.w_admin.common.base import AdminHandlerBase


@route(r'/admin_user_list', r'/admin_user_list/p(\d+)')
class AdminUserListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        page_index = int(page_index)

        users = AdminUserBLL.query(page_index, config.default_page_size)
        self.render('admin_user_list.html', users)
