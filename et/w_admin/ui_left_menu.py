# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from et.common.handler import UIModuleBase
from et.common.routing import UIModule
from et.w_admin.common.helper import web_helper
import config


@UIModule(r'LeftMenu')
class LeftMenuUIM(UIModuleBase):
    def render(self, menu, **kwargs):
        for k, v in kwargs.items():
            self.bag[k] = v

        self.bag.menu = menu
        return self.render_string('__left_menu_item.html')


@UIModule(r'SubMenu')
class SubMenuUIM(UIModuleBase):
    def render(self, pid, **kwargs):
        for k, v in kwargs.items():
            self.bag[k] = v

        user_info = web_helper.get_login_session(self.handler)
        if user_info:
            self.bag.menus = filter(lambda m: m.parent.id == pid, user_info.menus)
        return self.render_string('__sub_menu_item.html')
