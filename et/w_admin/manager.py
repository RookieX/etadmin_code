# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程


import os
import sys

import config

from et.common.helper import sys_path_extender

sys_path_extender.extend(config.third_party_path)

import tornado.web
import tornado.httpserver
import tornado.ioloop

from et.common.routing import route, UIModule
from et.common.helper import modules_importer

modules_importer.import_modules('.', '^handlers_.*\.py$')  # 加载handler文件，以便构造url映射
modules_importer.import_modules('.', '^ui_.*\.py$')  # 加载handler文件，以便构造ui module映射


class WebApp(tornado.web.Application):
    def __init__(self):
        super(WebApp, self).__init__(**make_settings())


def make_settings():
    u"""
        tornado用到的配置信息

        :rtype: dict
        :return: 配置字典
    """
    return {
        'debug': True,
        'autoreload': True,
        'handlers': route.routes(),
        'ui_modules': UIModule.moules(),
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
        'cookie_secret': '190qweasd$%^RTYFGH'
    }


def main():
    u"""
        启动应用程序
    """
    port = sys.argv[1]

    http_server = tornado.httpserver.HTTPServer(WebApp(), xheaders=True)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
