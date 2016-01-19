# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程

from et.common.handler import session_handler
from et.common.routing import url_route
from et.common.helper import ajax_helper

from et.w_admin.common.base import AdminHandlerBase, authentication
from et.w_admin.common import common_response
from et.w_admin.common.helper import admin_helper


@url_route.route(r'/login')
class LoginHandler(AdminHandlerBase):
    def get(self):
        self.render('login.html')

    def post(self):
        user_name = self.get_argument('user_name')
        password = self.get_argument('password')

        admin_helper.set_user_session(self, {'user_name': user_name, 'password': password})

        ajax_helper.write_json(self, {'status': 0})
