# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from ...model import Permission
from ...sql_helper import mysql_helper


class PermissionDAL(object):
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
