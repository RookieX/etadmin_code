# -*- coding: utf-8 -*-
# Date: 16-4-14
# Author: 徐鹏程

u"""
    后台用户类型
"""
# 国内用户
domestic_user = 1

# 所有用户类型的元组，方便html遍历渲染
all_types = (
    (domestic_user, u'国内用户'),
)

__types_dict = dict(all_types)


def type_name(user_type_value):
    """
        根据用户类型值获取名称
        :param user_type_value: 用户类型值
        :type user_type_value: int

        :rtype: str
    """
    return __types_dict[user_type_value]
