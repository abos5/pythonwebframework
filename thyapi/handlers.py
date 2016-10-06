#-*- coding: utf-8 -*-
from tornado import web
from tornado import gen


class IndexHandler(web.RequestHandler):

    @gen.coroutine
    def get(self):
        self.write('Hello, human.')
        self.finish()


# eof
