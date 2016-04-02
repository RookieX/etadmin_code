# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程

from et.bll.admin import DepartmentBLL
from et.common.routing.url_route import route
from et.w_admin import config
from et.w_admin.common.base import AdminHandlerBase


@route(r'/department_list', r'/department_list/(\d*)')
class DepartmentListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        departments = DepartmentBLL.query(page_index, config.default_page_size)
        self.render('department_list.html', departments)
