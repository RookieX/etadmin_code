# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程

from et.common.routing import route
from et.common.helper import ajax_helper

from et.bll.admin import AdminUserBLL

from et.w_admin.common.base import AdminHandlerBase
from et.w_admin.common.helper import web_helper

import config


@route(r'/login')
class LoginHandler(AdminHandlerBase):
    def get(self):
        self.render('login.html')

    def post(self):
        args = self.get_arguments_dict(['user_name', 'password'])

        if not args['user_name'] or not args['password']:
            return ajax_helper.write_json(self, -1, u'用户名或密码不能为空')

        if not AdminUserBLL.login(**args):
            return ajax_helper.write_json(self, -2, u'用户名或密码错误')

        # 读取用户详细信息，写入session
        user = AdminUserBLL.query_full_by_user_name(args['user_name'])

        web_helper.set_login_session(self, user)

        # 返回来源页面
        from_url = self.get_argument('from_url', '/')

        ajax_helper.write_json(self, 0, data={'redirect': from_url})


@route(r'/logout')
class LogoutHandler(AdminHandlerBase):
    def get(self):
        web_helper.remove_login_session(self)

        self.redirect('/login')
