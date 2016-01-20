# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

u'''
    mysql数据库访问帮助类
'''

import MySQLdb
import MySQLdb.cursors
import MySQLdb.connections

import config


def open_read_db():
    u'''
        打开只读库
    '''
    return ReadConnection(**_read_db_config)


def open_write_db():
    u'''
        打开可写库
    '''
    return WriteConnection(**_write_db_config)


def query(sql, params=None):
    u'''
        执行sql，返回数据库记录
    '''
    with open_read_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql, params)
        return cursor.fetchall()


def query_one(sql, params=None):
    u'''
        执行sql，只返回一条数据库记录。
        如果没有数据，返回None
    '''
    with open_read_db() as db:
        cursor = db.cursor(MySQLdb.cursors.DictCursor)
        if cursor.execute(sql, params):
            return cursor.fetchone()
        return None


def query_scalar(sql, params=None): pass


def execute_non_query(sql, params=None): pass


class MySqlDbConnBase(MySQLdb.connections.Connection):
    u'''
        mysql connection基类
    '''

    def __init__(self, *args, **kwargs):
        super(MySqlDbConnBase, self).__init__(*args, **kwargs)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class ReadConnection(MySqlDbConnBase):
    u'''
        只读库
    '''
    pass


class WriteConnection(MySqlDbConnBase):
    u'''
        可写库
    '''


# 只读库配置
_read_db_config = {
    'host': config.read_db_host,
    'port': config.read_db_port,
    'user': config.read_db_user,
    'passwd': config.read_db_pwd,
    'db': config.read_db_name
}

# 可写库配置
_write_db_config = {
    'host': config.write_db_host,
    'port': config.write_db_port,
    'user': config.write_db_user,
    'passwd': config.write_db_pwd,
    'db': config.write_db_name
}

if __name__ == '__main__':
    print query_one('select * from admin_user')
