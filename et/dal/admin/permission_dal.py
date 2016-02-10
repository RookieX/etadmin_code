# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from ...common.extend.type_extend import null
from ...model import Permission
from ...sql_helper import mysql_helper


class PermissionDAL(object):
    @staticmethod
    def query(start, end):
        u"""
            分页查询权限

            :param start: 开始记录行
            :param end: 结束记录行


            :rtype: list[Permission]
            :return: 权限列表
        """

        sql = u'''
            SELECT  id,
                    `name`,
                    description,
                    `order`,
                    create_datetime,
                    update_datetime
            FROM permission
            LIMIT %s,%s
        '''

        args = (start - 1, end - start)

        datas = mysql_helper.query(sql, args)
        return [Permission.build_from_dict(data) for data in datas]

    @staticmethod
    def query_by_user_name(user_name):
        u"""
            根据用户名获取用户的权限

            :param user_name:用户名

            :type user_name: str

            :return: 权限列表
            :rtype: list(permission)
        """
        sql = u'''
            SELECT  id,
                    `name`,
                    `order`
            FROM permission AS perm
            LEFT JOIN admin_user_permission_mapping AS map
            ON perm.id = map.permission_id
            WHERE map.user_name = %s
        '''
        args = (user_name,)

        datas = mysql_helper.query(sql, args)

        return [Permission.build_from_dict(data) for data in datas]

    @staticmethod
    def query_by_id(permission_id):
        u"""
            根据id查询权限

            :param permission_id: 权限id

            :type permission_id: int

            :rtype: Permission
            :return: 权限
        """

        sql = u'''
            SELECT  id,
                    `name`,
                    description,
                    `order`,
                    create_datetime,
                    update_datetime
            FROM permission
            WHERE id = %s
        '''

        args = (permission_id,)

        data = mysql_helper.query_one(sql, args)

        if data:
            return Permission.build_from_dict(data)

        return null

    @staticmethod
    def add(permission):
        u"""
            添加权限

            :param permission: 要添加的权限

            :type permission: Permission

            :rtype: int
            :return: 受影响行数
        """

        sql = u'''
            INSERT INTO permission
            (
              `name`,
              description,
              `order`,
              create_datetime,
              update_datetime
            )
            VALUES
            (
              %s,%s,%s,%s,%s
            )
        '''
        args = (permission.name,
                permission.description,
                permission.order,
                permission.create_datetime,
                permission.update_datetime)

        return mysql_helper.execute_non_query(sql, args)

    @staticmethod
    def update(permission):
        u"""
            更新权限

            :param permission: 要更新的权限

            :type permission: Permission

            :rtype: int
            :return: 受影响行数
        """
        sql = u'''
            UPDATE permission
            SET `name`=%s,
                description=%s,
                `order`=%s,
                update_datetime=%s
            WHERE id = %s
        '''

        args = (permission.name,
                permission.description,
                permission.order,
                permission.update_datetime,
                permission.id)

        return mysql_helper.execute_non_query(sql, args)
