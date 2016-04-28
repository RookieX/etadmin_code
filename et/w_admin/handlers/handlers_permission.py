# -*- coding: utf-8 -*-
# Date: 16-2-10
# Author: 徐鹏程


from et.common.helper import ajax_helper
from et.common.routing import route
from et.common.extend.type_extend import null

from et.bll.admin import PermissionBLL

from et.model import Permission

from et.w_admin import config
from et.w_admin.common.base import AdminHandlerBase


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
        permission = null

        if permission_id:

            permission = PermissionBLL.query_by_id(permission_id)
            if not permission:
                return self.error(u'没有找到这个权限')

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
            result = PermissionBLL.update(permission)
        else:
            result = PermissionBLL.add(permission)

        if result:
            return ajax_helper.write_success(self)

        ajax_helper.write_error(self)
