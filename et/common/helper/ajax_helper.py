# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    ajax帮助类
'''

import json


def write_json(handler, status, msg='', data=None):
    u'''
        向响应流中写入json数据

    '''

    handler.set_header('Content-Type', 'application/json')
    handler.write(json.dumps({'status': status, 'msg': msg, data: data}))
