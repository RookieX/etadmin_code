# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程


from et.common.handler import UIModuleBase
from et.common.routing import UIModule


@UIModule(r'TopMenuItem')
class TopMenuItemUIM(UIModuleBase):
    def render(self, menu, **kwargs):
        self.bag.menu = menu
        for k, v in kwargs.items():
            self.bag[k] = v
        return self.render_string('__top_menu_item.html')
