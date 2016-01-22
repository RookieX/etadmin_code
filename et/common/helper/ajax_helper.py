# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    ajax帮助类
"""

import json


def write_json(handler, status, msg='', data=None):
    u"""
        向响应流中写入json数据

        :param handler: HttpHandler
        :param status: 返回给浏览器的状态值
        :param msg: 返回给浏览器的文字消息
        :param data: 返回给浏览器的对象

        :type handler: et.common.handler.BaseHandler
        :type status: int
        :type msg: str
        :type data: dict
    """

    handler.set_header('Content-Type', 'application/json')
    handler.write(json.dumps({'status': status, 'msg': msg, 'data': data}))
