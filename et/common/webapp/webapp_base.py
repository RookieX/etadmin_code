# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程

import os

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.autoreload

from ..routing.url_route import route
from ..routing.ui_module_route import UIModule
from ..helper import modules_importer


class WebApp(tornado.web.Application):
    u"""
        WebApp基类，封装tornado
    """

    # tornado基本配置
    __app_settings = {
        'debug': True,
        'autoreload': False,
        'cookie_secret': '190qweasd$%^RTYFGH'
    }

    def __init__(self, handler_path=None, **settings):
        u"""
            :param handler_path: handler文件路径
            :param settings: webapp配置

            :type handler_path: str
            :type settings: dict
            
        """
        # 默认handlers路径为程序启动目录下的handlers目录
        handler_path = handler_path if handler_path else os.path.join(os.getcwd(), 'handlers')

        modules_importer.import_modules(handler_path, '^handlers_.*\.py$')  # 加载handler文件，以便构造url映射
        modules_importer.import_modules(handler_path, '^ui_.*\.py$')  # 加载handler文件，以便构造ui module映射

        # url路由
        self.__app_settings['handlers'] = route.routes()

        # ui_module路由
        self.__app_settings['ui_modules'] = UIModule.moules()

        self.__app_settings.update(settings)

        super(WebApp, self).__init__(**self.__app_settings)

    def run_server(self, port=80):
        u"""
            启动webapp

            :param port: webapp监听的端口号，默认80

            :type port: int
        """
        http_server = tornado.httpserver.HTTPServer(self, xheaders=True)
        http_server.listen(port)
        io_loop = tornado.ioloop.IOLoop.instance()

        # 5s reload
        tornado.autoreload.start(io_loop, check_time=5000)
        io_loop.start()
