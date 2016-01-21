# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程

from et.common.handler import session_handler
from et.common.routing import url_route
from et.common.helper import ajax_helper

from et.bll.admin import AdminUserBLL
from et.model import AdminUser

from et.w_admin.common.base import AdminHandlerBase, authentication
from et.w_admin.common import common_response
from et.w_admin.common.helper import admin_helper


@url_route.route(r'/login')
class LoginHandler(AdminHandlerBase):
    def get(self):
        self.render('login.html')

    def post(self):
        args = self.get_arguments_dict(['user_name', 'password'])

        if not args['user_name'] or not args['password']:
            return ajax_helper.write_json(self, -1, u'用户名或密码不能为空')

        if not AdminUserBLL.login(**args):
            return ajax_helper.write_json(self, -2, u'用户名或密码错误')

        user = AdminUserBLL.query_by_user_name(args['user_name'])

        admin_helper.set_user_session(self, user)

        ajax_helper.write_json(self, 0)
