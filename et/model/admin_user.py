# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

from ..common.extend.type_extend import null
from .model_base import ModelBase


class AdminUser(ModelBase):
    def __init__(self):
        self.__id = null
        self.__user_name = null
        self.__display_name = null
        self.__password = null
        self.user_type = null
        self.create_datetime = null
        self.update_datetime = null
        self.department = null
        self.position = null
        self.parent_position = null
