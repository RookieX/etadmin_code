# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

u"""
    通用响应
"""

import urllib

from et.common.helper import ajax_helper


def resp_auth_fail_json(handler, *args, **kwargs):
    u"""
        权限认证失败ajax响应

        :param handler: BaseHandler
        :param args: 其他参数
        :param kwargs: 其他参数

        :type handler: BaseHandler
        :type args: tuple
        :type kwargs: dict
    """
    ajax_helper.write_json(handler, {
        'status': -1,
        'msg': u'您没有权限进行此操作，请重新登录或联系您的主管。'
    })


def resp_auth_fail_regular(handler, *args, **kwargs):
    u"""
        权限认证失败一般响应

        :param handler: BaseHandler
        :param args: 其他参数
        :param kwargs: 其他参数

        :type handler: BaseHandler
        :type args: tuple
        :type kwargs: dict
    """
    handler.set_header('Content-Type', 'text/plain; charset=utf-8')
    handler.write(u'没有权限')


def resp_need_login_json(handler, *args, **kwargs):
    u"""
        需要登录ajax响应

        :param handler: BaseHandler
        :param args: 其他参数
        :param kwargs: 其他参数

        :type handler: BaseHandler
        :type args: tuple
        :type kwargs: dict
    """
    ajax_helper.write_json(handler, status=1, msg=u'请先登录')


def resp_need_login_regular(handler, *args, **kwargs):
    u"""
        需要登录一般响应

        :param handler: BaseHandler
        :param args: 其他参数
        :param kwargs: 其他参数

        :type handler: BaseHandler
        :type args: tuple
        :type kwargs: dict
    """
    handler.set_header('Content-Type', 'text/html')
    handler.render('need_login.html')
