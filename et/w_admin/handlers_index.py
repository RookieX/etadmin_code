# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from et.common.routing import route

from et.w_admin.common import common_response, permissions
from et.w_admin.common.base import AdminHandlerBase, authentication


@route(r'/')
class IndexHandler(AdminHandlerBase):
    @authentication(permissions.perm_home, common_response.resp_auth_fail_regular,
                    common_response.resp_need_login_regular)
    def get(self):
        self.render('index.html')
