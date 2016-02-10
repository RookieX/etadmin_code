# -*- coding: utf-8 -*-
# Date: 16-1-19
# Author: 徐鹏程

import sys

from ..common.helper import sys_path_extender

import config

sys_path_extender.extend(config.third_party_path)

from ali_memcached import AliMemcached
from local_cache import LocalCache
from local_memcached import LocalMemcached