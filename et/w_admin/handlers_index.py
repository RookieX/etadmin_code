# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from et.common.routing import url_route

from et.w_admin.common.base import AdminHandlerBase


@url_route.route(r'/')
class IndexHandler(AdminHandlerBase):
    def get(self):
        self.render('index.html')
