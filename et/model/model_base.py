# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

u"""
    Model基类
"""

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

        for name, value in properties.items():
            if hasattr(obj, name):
                setattr(obj, name, value if value is not None else null)

        return obj
