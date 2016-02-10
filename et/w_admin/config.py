# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程
u"""
    站点通用配置
"""

import os

# 第三方包路径
third_party_path = os.path.abspath(os.path.join(__file__, '../third_parties'))

# login session key
login_session_key = 'LOGINSESSION'

# 顶级菜单level
top_menu_level = 0

# 一级菜单level
primary_menu_level = 1

# 二级菜单level
secondary_menu_level = 2

# 默认分页大小
default_page_size = 20
