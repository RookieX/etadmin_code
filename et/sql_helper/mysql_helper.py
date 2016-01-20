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


class MySqlDbConnBase(MySQLdb.connections.Connection):
    u'''
        mysql connection基类
    '''

    def __init__(self, *args, **kwargs):
        super(MySqlDbConnBase, self).__init__(*args, **kwargs)


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
