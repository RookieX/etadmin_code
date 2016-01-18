# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程


import os
import sys

import config

from et.common.helpers import sys_path_extender

sys_path_extender.extend(config.third_party_path)

import tornado.web
import tornado.httpserver
import tornado.ioloop


class WebApp(tornado.web.Application):
    def __init__(self):
        super(self.__class__, self).__init__(**mk_settings())


class PingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')


def mk_settings():
    return {
        'handlers': [(r'/ping', PingHandler)],
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'template_path': os.path.join(os.path.dirname(__file__), 'templates')
    }


def main():
    port = sys.argv[1]

    http_server = tornado.httpserver.HTTPServer(WebApp(), xheaders=True)
    http_server.listen(port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
