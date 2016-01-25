# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from et.common.handler import UIModuleBase
from et.common.routing import UIModule

from et.w_admin.common.helper import web_helper


@UIModule(r'LeftMenu')
class LeftMenuUIM(UIModuleBase):
    def render(self, **kwargs):
        for k, v in kwargs.items():
            self.bag[k] = v
        user_info = web_helper.get_login_session(self.handler)

        self.bag.menus = []
        if user_info:
            self.bag.menus = user_info.menus

        return self.render_string('__left_menu.html')
