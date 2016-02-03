# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

u"""
    mysql数据库访问帮助类
"""

import MySQLdb
import MySQLdb.cursors
import MySQLdb.connections

import config


class MySqlDbConnBase(MySQLdb.connections.Connection):
    u"""
        mysql connection基类
    """

    def __init__(self, *args, **kwargs):
        super(MySqlDbConnBase, self).__init__(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class ReadConnection(MySqlDbConnBase):
    u"""
        只读库
    """
    pass


class WriteConnection(MySqlDbConnBase):
    u"""
        可写库
    """


def open_read_db():
    u"""
        打开只读库

        :rtype: ReadConnection
        :return: 只读数据库链接
    """
    return ReadConnection(**_read_db_config)


def open_write_db():
    u"""
        打开可写库

        :rtype: WriteConnection
        :return: 可写数据库链接
    """
    return WriteConnection(**_write_db_config)


def query(sql, params=None):
    u"""
        执行sql，返回数据库记录

        :param sql: sql语句
        :param params: sql参数

        :type sql: str
        :type params: tuple

        :rtype: tuple
    """
    with open_read_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql, params)
        return cursor.fetchall()


def query_one(sql, params=None):
    u"""
        执行sql，只返回一条数据库记录。
        如果没有数据，返回None

        :param sql: sql语句
        :param params: sql参数

        :type sql: str
        :type params: tuple

        :rtype: dict
    """
    with open_read_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        if cursor.execute(sql, params):
            return cursor.fetchone()
        return None


def query_scalar(sql, params=None):
    u"""
        执行sql，返回第一行第一列的值。
        如果没有数据，返回None

        :param sql: sql语句
        :param params: sql参数

        :type sql: str
        :type params: tuple
    """
    with open_read_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        if cursor.execute(sql, params):
            row, first_column = cursor.fetchone(), cursor.description[0][0]
            return row[first_column]

        return None


def execute_non_query(sql, params=None):
    u"""
        执行sql，返回受影响行数。

        :param sql: sql语句
        :param params: sql参数

        :type sql: str
        :type params: tuple

        :rtype: int
        :return: 受影响行数
    """
    with open_write_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        row_count = cursor.execute(sql, params)
        db.commit()
        return row_count


# 只读库配置
_read_db_config = {
    'host': config.read_db_host,
    'port': config.read_db_port,
    'user': config.read_db_user,
    'passwd': config.read_db_pwd,
    'db': config.read_db_name,
    'charset': config.read_db_charset
}

# 可写库配置
_write_db_config = {
    'host': config.write_db_host,
    'port': config.write_db_port,
    'user': config.write_db_user,
    'passwd': config.write_db_pwd,
    'db': config.write_db_name,
    'charset': config.write_db_charset
}

if __name__ == '__main__':
    with open_read_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        print cursor.execute('select * from admin_user')
