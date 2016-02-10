# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from datetime import datetime

from ...dal.admin import PermissionDAL
from ...model import Permission

from ..common.helper import page_helper


class PermissionBLL(object):
    @staticmethod
    def query(page_index, page_size):
        u"""
            分页查询权限

            :param page_index: 页号
            :param page_size: 分页大小

            :type page_index: int
            :type page_size: int

            :rtype: list[Permission]
            :return: 权限列表
        """

        start, end = page_helper.calc_page_range(page_index, page_size)
        return PermissionDAL.query(start, end)

    @staticmethod
    def query_by_id(permission_id):
        u"""
            根据id查询权限

            :param permission_id: 权限id

            :type permission_id: int

            :rtype: Permission
            :return: 权限
        """

        return PermissionDAL.query_by_id(permission_id)

    @staticmethod
    def add(permission):
        u"""
            添加权限

            :param permission: 要添加的权限

            :type permission: Permission

            :rtype: bool
            :return: 添加是否成功
        """

        permission.create_datetime = permission.update_datetime = datetime.now()

        return PermissionDAL.add(permission) == 1

    @staticmethod
    def update(permission):
        u"""
            更新权限

            :param permission: 要更新的权限

            :type permission: Permission

            :rtype: bool
            :return: 更新是否成功
        """

        permission.update_datetime = datetime.now()

        return PermissionDAL.update(permission) == 1
