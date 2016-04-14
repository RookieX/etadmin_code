# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

u"""
    Model基类
"""
import re
import inspect
from collections import Iterable

from ..common.extend.type_extend import null


class ModelBase(object):
    u"""
        Model基类，提供Model通用属性和方法
    """

    @classmethod
    def build_from_dict(cls, properties):
        u"""
            利用字典对象构造Model

            :param properties: Model需要的属性
            :type properties: dict

            :rtype: ModelBase
            :return: ModelBase
        """

        obj = cls()

        if not properties:
            return obj

        for name, value in properties.items():
            if hasattr(obj, name):
                setattr(obj, name, value if value is not None else null)

        return obj

    def to_dict(self):
        u"""
            将Model转化为dict

            :rtype: dict
        """

        data = {}

        re_pattern = r'^_{0}__(\w*)'.format(self.__class__.__name__)

        for key, value in self.__dict__.items():
            if key in data:
                continue
            matches = re.match(re_pattern, key)

            if matches:
                value = None if value == null else value
                value = value.to_dict if isinstance(value, ModelBase) else value

                if inspect.isroutine(value):
                    continue

                if not isinstance(value, basestring) and isinstance(value, Iterable):
                    temp = []
                    for i, item in enumerate(value):
                        if isinstance(item, ModelBase):
                            temp.append(item.to_dict())
                    value = temp

                data[matches.group(1)] = value
        return data
