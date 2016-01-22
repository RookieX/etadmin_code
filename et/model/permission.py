# -*- coding: utf-8 -*-
# Date: 16-1-21
# Author: 徐鹏程

from ..common.extend.type_extend import null
from .model_base import ModelBase


class Permission(ModelBase):
    def __init__(self):
        self.__id = null
        self.__name = null
        self.__description = null
        self.__order = null

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
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
