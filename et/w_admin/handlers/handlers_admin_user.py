# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程

from et.common.routing.url_route import route
from et.common.extend.type_extend import null

from et.bll.admin import AdminUserBLL
from et.bll.admin import PositionBLL
from et.bll.admin import DepartmentBLL

from et.w_admin import config
from et.w_admin.common.base import AdminHandlerBase
from et.w_admin.common.enums import UserType


@route(r'/admin_user_list', r'/admin_user_list/p(\d+)')
class AdminUserListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        page_index = int(page_index)

        users = AdminUserBLL.query(page_index, config.default_page_size)
        self.render('admin_user_list.html', users)


@route(r'/admin_user_edit', r'/admin_user_edit/(\w*)')
class AdminUserEditHandler(AdminHandlerBase):
    def get(self, admin_user_name=''):
        admin_user = null
        if admin_user_name:
            admin_user = AdminUserBLL.query_full_by_user_name(admin_user_name)
        self.bag.user_types = UserType.all_types
        self.bag.positions = PositionBLL.query_all()
        self.bag.departments = DepartmentBLL.query_all()

        self.render('admin_user_edit.html', admin_user)
