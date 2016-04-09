# -*- coding: utf-8 -*-
# Date: 16-4-9
# Author: 徐鹏程

from datetime import datetime

from ...dal.admin import PositionDAL
from ...model import Position

from ..common.helper import page_helper


class PositionBLL(object):
    @staticmethod
    def query(page_index, page_size):
        u"""
            分页查询职位

            :param page_index: 页号
            :param page_size: 分页大小

            :type page_index: int
            :type page_size: int

            :rtype: list[Position]
            :return: 职位列表
        """

        start, end = page_helper.calc_page_range(page_index, page_size)
        return PositionDAL.query(start, end)

    @staticmethod
    def query_all():
        u"""
            查询所有职位

            :return: 所有职位
            :rtype: list[Position]
        """
        return PositionDAL.query_all()

    @staticmethod
    def query_by_id(pos_id):
        u"""
            根据id查找职位

            :param pos_id: 职位id
            :type pos_id: int

            :return: 职位
            :rtype: Position
        """
        return PositionDAL.query_by_id(pos_id)

    @staticmethod
    def query_by_level(level):
        u"""
            根据level查询职位

            :param level: 级别
            :type level: int

            :return: 级别列表
            :rtype: list[Position]
        """
        return PositionDAL.query_by_level(level)

    @staticmethod
    def add(position):
        u"""
            添加职位

            :param position: 职位
            :type position: Position

            :return: 添加是否成功
            :rtype: bool
        """

        position.create_datetime = position.update_datetime = datetime.now()
        position.parent.id = int(position.parent.id) if position.parent.id else 0
        return PositionDAL.add(position) == 1

    @staticmethod
    def update(position):
        u"""
            更新职位

            :param position: 职位
            :type position: Position

            :return: 更新是否成功
            :rtype: bool
        """

        position.update_datetime = datetime.now()
        position.parent.id = int(position.parent.id) if position.parent.id else 0
        return PositionDAL.update(position) == 1
