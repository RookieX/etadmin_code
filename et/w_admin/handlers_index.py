# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from et.common.routing import route

from et.w_admin.common import common_response, permissions
from et.w_admin.common.base import AdminHandlerBase, authentication
from et.w_admin.common.helper import web_helper
import config


@route(r'/')
class IndexHandler(AdminHandlerBase):
    @authentication(permissions.perm_home, common_response.resp_auth_fail_regular,
                    common_response.resp_need_login_regular)
    def get(self):
        self.render('index.html')


@route(r'/top')
class TopHandler(AdminHandlerBase):
    def get(self):
        user_info = web_helper.get_login_session(self)
        if user_info:
            self.bag.menus = filter(lambda m: m.level == config.top_menu_level, user_info.menus)

        self.render('top.html')


@route(r'/left')
@route(r'/left/(\d*)')
class LeftHandler(AdminHandlerBase):
    def get(self, pid=-1, **kwargs):

        if pid == -1:
            # 没有父菜单ID，默认取部门默认父菜单
            pass
        else:
            pid = int(pid)

        user_info = web_helper.get_login_session(self)
        if user_info:
            self.bag.menus = filter(lambda m: m.level == config.primary_menu_level and m.parent.id == pid,
                                    user_info.menus)
        self.render('left.html')
