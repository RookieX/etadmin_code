# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程

from et.common.routing.url_route import route
from et.common.extend.type_extend import null
from et.common.helper import ajax_helper
from et.common.helper import encrypt_helper

from et.bll.admin import AdminUserBLL
from et.bll.admin import PositionBLL
from et.bll.admin import DepartmentBLL

from et.model import AdminUser
from et.model import Position

from et.w_admin import config
from et.w_admin.common.base import AdminHandlerBase
from et.w_admin.common.enums import UserType


@route(r'/admin_user_list', r'/admin_user_list/p(\d+)')
class AdminUserListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        page_index = int(page_index)

        users = AdminUserBLL.query(page_index, config.default_page_size)
        self.render('admin_user_list.html', users)


@route(r'/admin_user_edit', r'/admin_user_edit/(\w*)')
class AdminUserEditHandler(AdminHandlerBase):
    def get(self, admin_user_name=''):
        admin_user = null
        if admin_user_name:
            admin_user = AdminUserBLL.query_full_by_user_name(admin_user_name)

            if not admin_user:
                return self.error(u'没有找到这个用户')

        self.bag.user_types = UserType.all_types
        self.bag.positions = PositionBLL.query_all()
        self.bag.departments = DepartmentBLL.query_all()

        self.bag.is_update = bool(admin_user_name)

        self.render('admin_user_edit.html', admin_user)

    def post(self, admin_user_name=''):
        arguments = self.get_arguments_dict(['display_name', 'password', 'user_type', 'position_id'])
        user = AdminUser.build_from_dict(arguments)
        user.user_name = admin_user_name
        user.user_type = int(user.user_type)
        user.position = Position.build_from_dict({'id': arguments['position_id']})
        if user.password:
            user.password = encrypt_helper.password(user.password)

        is_update = self.get_argument('is_update')

        # 更新
        if is_update == 'True':
            result = AdminUserBLL.update(user)
        # 新增
        else:
            result = AdminUserBLL.add(user)

        if result:
            return ajax_helper.write_success(self)

        ajax_helper.write_error(self)
