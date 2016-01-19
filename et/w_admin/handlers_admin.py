# -*- coding: utf-8 -*-
# Date: 16-1-18
# Author: 徐鹏程

from et.common.handler import session_handler
from et.common.routing import url_route


@url_route.route(r'/login')
class LoginHandler(session_handler.SessionHandler):
    def get(self):
        self.render('login.html')
