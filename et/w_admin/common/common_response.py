# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u'''
    通用响应
'''

from et.common.helper import ajax_helper


def resp_auth_fail_json(handler):
    u'''
        权限认证失败ajax响应
    '''
    ajax_helper.write_json(handler, {
        'status': -1,
        'msg': u'您没有权限进行此操作，请重新登录或联系您的主管。'
    })


def resp_auth_fail_regular(handler):
    u'''
        权限认证失败一般响应
    '''
    handler.write(u'没有权限')
