#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#
from tornado.testing import AsyncHTTPTestCase, gen_test
from tornado.httpclient import AsyncHTTPClient
import frontend


class FooTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return frontend.make_app()

    @gen_test
    def test_foo(self):
        client = AsyncHTTPClient()
        response = yield client.fetch(
            'http://localhost:%d/' % self.get_http_port(),
        )
        self.assertEquals('Hello, human.', response.body)




# eof
