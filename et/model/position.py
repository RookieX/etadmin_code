# -*- coding: utf-8 -*-
# Date: 16-4-8
# Author: 徐鹏程

from ..common.extend.type_extend import null
from .model_base import ModelBase


class Position(ModelBase):
    def __init__(self):
        self.__id = null
        self.__name = null
        self.__level = null
        self.__parent = null
        self.__create_datetime = null
        self.__update_datetime = null

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__level = value

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        self.__parent = value

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
