# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

u"""
    UIModule基类
"""
import tornado.web

from ..extend.type_extend import dynamic


class UIModuleBase(tornado.web.UIModule):
    def __init__(self, *args, **kwargs):
        super(UIModuleBase, self).__init__(*args, **kwargs)
        self.bag = dynamic()

    def render_string(self, template_path, **kwargs):
        u"""
            覆盖父类的render_string，提供bag统一给template传参数

            :param template_path: template路径

            :type template_path: str
        """
        return super(UIModuleBase, self).render_string(template_path, bag=self.bag)
