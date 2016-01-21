# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from et.common.routing import url_route

from et.w_admin.common import common_response
from et.w_admin.common.base import AdminHandlerBase, login


@url_route.route(r'/')
class IndexHandler(AdminHandlerBase):
    @login(common_response.resp_need_login_regular)
    def get(self):
        self.render('index.html')
