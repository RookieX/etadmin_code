# -*- coding: utf-8 -*-
# Date: 16-1-20
# Author: 徐鹏程

u"""
    加解密相关帮助方法
"""

import hashlib
import hmac


def password(plain):
    u"""
        对密码进行加密
        :param plain:要加密的字符串

        :type plain:str

        :rtype: str
        :return: 加密后的字符串
    """
    if plain is None:
        return ''

    return hashlib.sha1(plain.encode('utf-8') + '12qw#$ERDF56tyghbn').hexdigest()


def encrypt(plain):
    if plain is None:
        return ''

    return hashlib.sha1(plain.encode('utf-8') + '323deasytransfer!python').hexdigest()


def gen_hmac(data, key='test', enc='gb2312'):
    str = ''.join(data).encode(enc)
    print str
    hs = hmac.new(key)
    hs.update(str)

    return hs.hexdigest()


def gen_md5(data, enc='utf-8'):
    m = hashlib.md5()
    m.update(data.encode(enc))
    return m.hexdigest()
