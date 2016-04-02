# -*- coding: utf-8 -*-
# Date: 16-1-31
# Author: 徐鹏程

import math

from et.common.handler import UIModuleBase
from et.common.routing import UIModule


@UIModule('Pager')
class PagerUIM(UIModuleBase):
    def render(self, url_format, total_count, page_size, current_page, **kwargs):
        super(PagerUIM, self).render(**kwargs)

        self.bag.url_format = url_format
        self.bag.total_count = total_count
        self.bag.page_count = math.ceil(total_count * 0.1 / page_size)
        self.bag.current_page = current_page

        self.render_string('__pager.html')
