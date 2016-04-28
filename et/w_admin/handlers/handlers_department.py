# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程

from et.common.helper import ajax_helper
from et.common.routing.url_route import route
from et.common.extend.type_extend import null
from et.bll.admin import DepartmentBLL
from et.bll.admin import MenuBLL
from et.model import Department
from et.model import Menu

from et.w_admin import config
from et.w_admin.common.base import AdminHandlerBase


@route(r'/department_list', r'/department_list/(\d*)')
class DepartmentListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        page_index = int(page_index)
        departments = DepartmentBLL.query(page_index, config.default_page_size)
        self.render('department_list.html', departments)


@route(r'/department_edit', r'/department_edit/(\d*)')
class DepartmentEditHandler(AdminHandlerBase):
    def get(self, dept_id=0):
        dept_id = int(dept_id)
        department = null
        if dept_id:
            department = DepartmentBLL.query_by_id(dept_id)
            if not department:
                return self.error(u'没有找到这个部门')

        top_menus = MenuBLL.query_by_level(config.top_menu_level)

        self.bag.menus = top_menus
        self.render('department_edit.html', department)

    def post(self, dept_id=0):
        arguments = self.get_arguments_dict(['name', 'default_menu'])

        dept = Department.build_from_dict(arguments)
        dept.default_top_menu = Menu.build_from_dict({'id': arguments['default_menu']})
        dept.id = dept_id
        # 更新
        if dept_id:
            result = DepartmentBLL.update(dept)
        else:  # 新增
            result = DepartmentBLL.add(dept)

        if result:
            return ajax_helper.write_success(self)

        ajax_helper.write_error(self)
