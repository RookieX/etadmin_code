# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    web基类
"""

import tornado.web

from ..extend.type_extend import dynamic


class BaseHandler(tornado.web.RequestHandler):
    u"""
        所有HttpRequest的基类
    """

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__(*args, **kwargs)

        self.bag = dynamic()

    def render(self, template_path, model=None):
        u"""
            覆盖父类的render，提供bag统一给template传参数

            :param template_path: template路径
            :param model: model

            :type template_path: str
        """
        super(BaseHandler, self).render(template_path, model=model, bag=self.bag)

    def get_arguments_dict(self, names, required=False, default=None, strip=True):
        u"""
            获取http请求参数字典

            :param names:要获取的参数名
            :param required:参数是否必须
            :param default:参数默认值
            :param strip:参数是否去掉前后空白

            :type names:list
            :type required:bool
            :type default:
            :type strip:bool

            :rtype: dict
            :return: 请求参数字典
        """

        args = {}

        for name in names:
            arg = self.get_argument(name, default, strip)
            if required and not arg:
                raise tornado.MissingArgumentError(name)

            args[name] = arg

        return args
