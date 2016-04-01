# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程


import os
import sys

import config

from et.common.helper import sys_path_extender

sys_path_extender.extend(config.third_party_path)

from et.common.webapp.webapp_base import WebApp


def make_settings():
    u"""
        tornado用到的配置信息

        :rtype: dict
        :return: 配置字典
    """
    return {
        'debug': True,
        'autoreload': True,
        'static_path': os.path.join(os.path.dirname(__file__), 'static'),
        'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
    }


def main():
    u"""
        启动应用程序
    """
    port = sys.argv[1]

    handler_path = os.path.abspath('.')
    WebApp(handler_path=handler_path, **make_settings()).run_server(port)


if __name__ == '__main__':
    main()
