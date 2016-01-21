# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ..common.extend.type_extend import null
from .model_base import ModelBase


class AdminUser(ModelBase):
    def __init__(self):
        self.__user_name = null
        self.__display_name = null
        self.__password = null
        self.__user_type = null
        self.__create_datetime = null
        self.__update_datetime = null
        self.__department = null
        self.__position = null
        self.__parent_position = null
        self.__permissions = []

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, value):
        self.__user_name = value

    @property
    def display_name(self):
        return self.__display_name

    @display_name.setter
    def display_name(self, value):
        self.__display_name = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def user_type(self):
        return self.__user_type

    @user_type.setter
    def user_type(self, value):
        self.__user_type = value

    @property
    def create_datetime(self):
        return self.__create_datetime

    @create_datetime.setter
    def create_datetime(self, value):
        self.__create_datetime = value

    @property
    def update_datetime(self):
        return self.__update_datetime

    @update_datetime.setter
    def update_datetime(self, value):
        self.__update_datetime = value

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def parent_position(self):
        return self.__parent_position

    @parent_position.setter
    def parent_position(self, value):
        self.__parent_position = value

    @property
    def permissions(self):
        return self.__permissions

    @permissions.setter
    def permissions(self, value):
        self.__permissions = value
