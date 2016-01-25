# -*- coding: utf-8 -*-
# Date: 16-1-25
# Author: 徐鹏程

from et.common.handler import UIModuleBase
from et.common.routing import UIModule

from et.w_admin.common.helper import web_helper
import config


@UIModule(r'MenuItem')
class MenuItemUIM(UIModuleBase):
    def render(self, level, parent_id, **kwargs):
        for k, v in kwargs.items():
            self.bag[k] = v
        user_info = web_helper.get_login_session(self.handler)
        if user_info:
            self.bag.menus = [menu for menu in user_info.menus if
                              menu.level == level and menu.parent.id == parent_id]

        if level == 1:
            return self.render_string('__primary_menu.html')
        elif level == 2:
            return self.render_string('__secondary_menu.html')
