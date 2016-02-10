# -*- coding: utf-8 -*-
# Date: 16-2-10
# Author: 徐鹏程

u""""
   分页帮助类
"""


def calc_page_range(page_index, page_size):
    u"""
        计算分页区间

        :param page_index: 页号
        :param page_size: 分页大小

        :type page_index: int
        :type page_size: int

        :rtype: tuple[int,int]
        :return: 分页区间
    """

    start = (page_index - 1) * page_size + 1
    end = start + page_size - 1

    return (start, end)
