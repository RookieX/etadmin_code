# -*- coding: utf-8 -*-
# Date: 16-1-22
# Author: 徐鹏程

from ..common.extend.type_extend import null
from .model_base import ModelBase


class Menu(ModelBase):
    def __init__(self):
        self.__id = null
        self.__name = null
        self.__display_name = null
        self.__description = null
        self.__level = null
        self.__parent = null
        self.__url = null
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
    def display_name(self):
        return self.__display_name

    @display_name.setter
    def display_name(self, value):
        self.__display_name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

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
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, value):
        self.__order = value
