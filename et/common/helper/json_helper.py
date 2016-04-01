# -*- coding: utf-8 -*-
# Date: 16-4-1
# Author: 徐鹏程
u"""josn帮助类"""

import json
import json.encoder
from datetime import datetime


def serialize(obj):
    u"""
        将对象序列化成json字符串
        :param obj: 要序列化的对象

        :rtype: str
    """

    return json.dumps(obj, cls=ETJSONEncoder)


def deserialize(json_str, obj_cls):
    u"""
        将json字符串反序列化成dict

        :param json_str:要反序列化的json字符串
        :param obj_cls:目标对象类型

        :type json_str:str
        :type obj_cls:object

        :rtype: object
    """
    pass


class ETJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super(ETJSONEncoder, self).default(o)


if __name__ == '__main__':
    print __file__.doc_string
