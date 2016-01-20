# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

u'''
    mysql数据库访问帮助类
'''

import functools

import MySQLdb
import MySQLdb.cursors
import MySQLdb.connections

import config


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


def read_db(func):
    u'''
        只读库装饰器
    '''

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        with open_read_db() as db:
            cursor = db.cursor(MySQLdb.cursors.DictCursor)
            return func(cursor, *args, **kwargs)

    return _wrapper


def write_db(func):
    u'''
        可写库装饰器
    '''

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        with open_write_db() as db:
            cursor = db.cursor(MySQLdb.cursors.DictCursor)
            return func(cursor, *args, **kwargs)

    return _wrapper


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


@read_db
def query(db, sql, params=None):
    u'''
        执行sql，返回数据库记录
    '''
    db.execute(sql, params)
    return db.fetchall()


@read_db
def query_one(db, sql, params=None):
    u'''
        执行sql，只返回一条数据库记录。
        如果没有数据，返回None
    '''

    if db.execute(sql, params):
        return db.fetchone()
    return None


@read_db
def query_scalar(db, sql, params=None):
    u'''
        执行sql，返回第一行第一列的值。
        如果没有数据，返回None
    '''
    if db.execute(sql, params):
        if db.rowcount:
            row, first_column = db.fetchone(), db.description[0][0]
            return row[first_column]

    return None


def execute_non_query(db, sql, params=None): pass


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
    print query_scalar('select user_name,display_name from admin_user')
