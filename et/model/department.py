# -*- coding: utf-8 -*-
# Date: 16-1-28
# Author: 徐鹏程

from ..common.extend.type_extend import null
from .model_base import ModelBase


class Department(ModelBase):
    def __init__(self):
        self.__id = null
        self.__name = null
        self.__default_top_menu = null

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
    def default_top_menu(self):
        return self.__default_top_menu

    @default_top_menu.setter
    def default_top_menu(self, value):
        self.__default_top_menu = value
