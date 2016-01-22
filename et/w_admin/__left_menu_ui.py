# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from et.common.handler import UIModuleBase
from et.common.routing import UIModule


@UIModule(r'LeftMenu')
class LeftMenuUIM(UIModuleBase):
    def render(self, **kwargs):
        for k, v in kwargs.items():
            self.bag[k] = v
        return self.render_string('__left_menu.html')
