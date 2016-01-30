# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from et.common.routing import route

from et.w_admin.common import common_response, permissions
from et.w_admin.common.base import AdminHandlerBase, authentication, login
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

        # 加载顶级菜单
        self.bag.menus = filter(lambda m: m.level == config.top_menu_level, user_info.menus)
        self.bag.display_name = user_info.display_name

        self.render('top.html')


@route(r'/left', r'/left/(\d*)')
class LeftHandler(AdminHandlerBase):
    @login(common_response.resp_need_login_regular)
    def get(self, parent_id=-1, **kwargs):
        user_info = web_helper.get_login_session(self)

        # 显示子菜单，parent_id==-1时，显示该部门默认菜单
        if parent_id == -1:
            parent_id = user_info.department.default_top_menu.id
        else:
            parent_id = int(parent_id)

        self.bag.menus = filter(lambda m: m.level == config.primary_menu_level and m.parent.id == parent_id,
                                user_info.menus)
        self.render('left.html')


@route(r'/logout')
class LogoutHandler(AdminHandlerBase):
    def get(self):
        web_helper.remove_login_session(self)

        self.redirect('/login')
