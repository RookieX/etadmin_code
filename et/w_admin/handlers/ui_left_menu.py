# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from et.common.handler import UIModuleBase
from et.common.routing import UIModule
from et.w_admin.common.helper import web_helper


@UIModule(r'LeftMenu')
class LeftMenuUIM(UIModuleBase):
    def render(self, menu, **kwargs):
        super(LeftMenuUIM, self).render(menu, **kwargs)

        self.bag.menu = menu
        return self.render_string('ui_modules/__left_menu_item.html')


@UIModule(r'SubMenu')
class SubMenuUIM(UIModuleBase):
    def render(self, pid, **kwargs):
        super(SubMenuUIM, self).render(**kwargs)

        user_info = web_helper.get_login_session(self.handler)

        self.bag.menus = filter(lambda m: m.parent.id == pid, user_info.menus)

        return self.render_string('ui_modules/__sub_menu_item.html')
