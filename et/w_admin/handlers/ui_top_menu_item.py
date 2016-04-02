# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程


from et.common.handler import UIModuleBase
from et.common.routing import UIModule


@UIModule(r'TopMenuItem')
class TopMenuItemUIM(UIModuleBase):
    def render(self, menu, **kwargs):
        super(TopMenuItemUIM, self).render(menu, **kwargs)
        self.bag.menu = menu
        return self.render_string('ui_modules/__top_menu_item.html')
