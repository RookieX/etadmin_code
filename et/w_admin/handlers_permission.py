# -*- coding: utf-8 -*-
# Date: 16-2-10
# Author: 徐鹏程


from et.common.routing import route
from et.common.extend.type_extend import null
from et.common.helper import ajax_helper

from et.bll.admin import PermissionBLL
from et.model import Permission

from et.w_admin.common.base import AdminHandlerBase

import config


@route(r'/permission_list', r'/permission_list/p(\d+)')
class PermissionListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        page_index = int(page_index)

        permissions = PermissionBLL.query(page_index, config.default_page_size)

        self.render('permission_list.html', permissions)


@route(r'/permission_edit', r'/permission_edit/(\d+)')
class PermissionEditHandler(AdminHandlerBase):
    def get(self, permission_id=0):
        permission_id = int(permission_id)

        permission = PermissionBLL.query_by_id(permission_id)

        self.render('permission_edit.html', permission)

    def post(self, permission_id=0):
        arguments = self.get_arguments_dict(['name', 'description', 'order'])

        if not arguments['name']:
            return ajax_helper.write_json(self, -1, u'请输入权限名')
        if not arguments['order']:
            return ajax_helper.write_json(self, -2, u'请输入排序')

        permission = Permission.build_from_dict(arguments)
        permission.id = permission_id

        if permission_id:
            self.update(permission)
        else:
            self.add(permission)

    def add(self, permission):
        if PermissionBLL.add(permission):
            return ajax_helper.write_json(self, 0)
        return ajax_helper.write_json(self, -1)

    def update(self, permission):
        if PermissionBLL.update(permission):
            return ajax_helper.write_json(self, 0)
        return ajax_helper.write_json(self, -1)
