# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from ..common.helper import page_helper

from ...model import Department
from ...dal.admin import DepartmentDAL


class DepartmentBLL(object):
    @staticmethod
    def query(page_index, page_size):
        u"""
            分页查询部门
            :param page_index: 页号
            :param page_size:  分页大小

            :type page_index: int
            :type page_size:  int

            :rtype: list[Department]
            :return: 部门列表
        """
        start, end = page_helper.calc_page_range(page_index, page_size)
        return DepartmentDAL.query(start, end)

    @staticmethod
    def find_by_id(dept_id):
        u"""
            根据部门id查找部门信息

            :param dept_id: 部门id
            :type dept_id: int

            :return: 部门信息
            :rtype: Department
        """

        return DepartmentDAL.find_by_id(dept_id)
