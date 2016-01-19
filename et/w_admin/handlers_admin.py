# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程

from et.common.handler import session_handler
from et.common.routing import url_route

from et.w_admin.common.base import AdminHandlerBase, authentication
from et.w_admin.common import common_response


@url_route.route(r'/login')
class LoginHandler(AdminHandlerBase):
    @authentication('', common_response.resp_auth_fail_json)
    def get(self):
        self.render('login.html')
