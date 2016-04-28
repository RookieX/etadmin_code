# -*- coding: utf-8 -*-
# Date: 16-4-8
# Author: 徐鹏程

from et.common.routing import route
from et.common.extend.type_extend import null
from et.common.helper import ajax_helper

from et.bll.admin import PositionBLL
from et.bll.admin import DepartmentBLL
from et.model import Position
from et.model import Department

from et.w_admin.common.base import AdminHandlerBase
from et.w_admin.common.helper import admin_helper
from et.w_admin import config


@route(r'/position_list', r'/position_list/(\d*)')
class PositionListHandler(AdminHandlerBase):
    def get(self, page_index=1):
        page_index = int(page_index)
        positions = PositionBLL.query(page_index, config.default_page_size)

        self.render('position_list.html', positions)


@route(r'/position_edit', r'/position_edit/(\d*)')
class PositionEditHandler(AdminHandlerBase):
    def get(self, pos_id=0):
        pos_id = int(pos_id)
        position = null

        if pos_id:
            position = PositionBLL.query_by_id(pos_id)
            if not position:
                return self.error(u'没有找到这个职位')

        if position:
            self.bag.positions = PositionBLL.query_by_level(position.level - 1)
        self.bag.departments = DepartmentBLL.query_all()

        self.render('position_edit.html', position)

    def post(self, pos_id=0):
        pos_id = int(pos_id)

        arguments = self.get_arguments_dict(['name', 'department_id', 'level', 'parent_position'])

        position = Position.build_from_dict(arguments)
        position.id = pos_id
        position.parent = Position.build_from_dict({'id': arguments['parent_position']})
        position.department = Department.build_from_dict({'id': arguments['department_id']})

        if pos_id:
            result = PositionBLL.update(position)
        else:
            result = PositionBLL.add(position)

        if result:
            return ajax_helper.write_success(self)

        ajax_helper.write_error(self)


@route(r'/load_positions')
class LoadPosotionsHandler(AdminHandlerBase):
    def get(self):
        level = self.get_argument('level', '')

        if not level:
            return ajax_helper.write_json(self, -1, u'请先输入正确的level')

        level = admin_helper.parse_int(level)
        positions = PositionBLL.query_by_level(level)
        ajax_helper.write_json(self, 0, data=[pos.to_dict() for pos in positions])
