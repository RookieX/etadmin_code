# -*- coding: utf-8 -*-
# Date: 16-4-9
# Author: 徐鹏程

from ...common.extend.type_extend import null
from ...sql_helper import mysql_helper
from ...model import Position
from ...model import Department


class PositionDAL(object):
    @staticmethod
    def query(start, end):
        u"""
            分页查询职位

            :param start: 页号
            :param end: 分页大小

            :type start: int
            :type end: int

            :rtype: list[Position]
            :return: 职位列表
        """

        args = (start - 1, end - start)

        sql = u'''
            SELECT  p.id,
                    p.name,
                    p.department_id,
                    dept.name AS dept_name,
                    p.level,
                    pp.name AS parent_position_name,
                    p.create_datetime,
                    p.update_datetime
            FROM position AS p
            LEFT JOIN position AS pp
            ON p.parent_position_id = pp.id
            LEFT JOIN department AS dept
            on p.department_id = dept.id
            LIMIT %s,%s
        '''

        datas = mysql_helper.query(sql, args)

        return [_build_position(data) for data in datas]

    @staticmethod
    def query_by_id(pos_id):
        u"""
            根据id查找职位

            :param pos_id: 职位id
            :type pos_id: int

            :return: 职位
            :rtype: Position
        """

        sql = u'''
            SELECT  id,
                    `name`,
                    `level`,
                    parent_position_id,
                    create_datetime,
                    update_datetime
            FROM position
            WHERE id = %s
        '''
        args = (pos_id,)
        data = mysql_helper.query_one(sql, args)
        return _build_position(data)

    @staticmethod
    def query_all():
        u"""
            查询所有职位

            :return: 所有职位
            :rtype: list[Position]
        """
        sql = u'''
            SELECT  id,
                    `name`,
                    `level`,
                    parent_position_id,
                    create_datetime,
                    update_datetime
            FROM position
        '''
        datas = mysql_helper.query(sql)
        return [_build_position(data) for data in datas]

    @staticmethod
    def query_by_level(level):
        u"""
            根据level查询职位

            :param level: 级别
            :type level: int

            :return: 级别列表
            :rtype: list[Position]
        """
        sql = u'''
            SELECT  id,
                    name
            FROM position
            WHERE `level` = %s
        '''
        args = (level,)
        datas = mysql_helper.query(sql, args)

        return [_build_position(data) for data in datas]

    @staticmethod
    def add(position):
        u"""
            添加职位

            :param position: 职位
            :type position: Position

            :return: 受影响行数
            :rtype: int
        """
        sql = u'''
            INSERT INTO position
            (
                `name`,
                department_id,
                `level`,
                parent_position_id,
                create_datetime,
                update_datetime
            )
            VALUES
            (%s,%s,%s,%s,%s,%s)
        '''
        args = (
            position.name,
            position.department.id,
            position.level,
            position.parent.id,
            position.create_datetime,
            position.update_datetime
        )

        return mysql_helper.execute_non_query(sql, args)

    @staticmethod
    def update(position):
        u"""
            更新职位

            :param position: 职位
            :type position: Position

            :return: 受影响行数
            :rtype: int
        """
        sql = u'''
            UPDATE position
            SET `name`=%s,
                parent_position_id=%s,
                update_datetime=%s
            WHERE id=%s
        '''
        args = (
            position.name,
            position.parent.id,
            position.update_datetime,
            position.id
        )

        return mysql_helper.execute_non_query(sql, args)


def _build_position(data):
    u"""
        构造职位信息

        :param data: 职位信息
        :type data: dict

        :return: 职位
        :rtype: Position
    """
    pos = Position.build_from_dict(data)
    pos.parent = Position.build_from_dict(
        {'id': data.get('parent_position_id', null), 'name': data.get('parent_position_name', null)})
    pos.department = Department.build_from_dict(
        {'id': data.get('department_id', null), 'name': data.get('dept_name', null)})
    return pos
