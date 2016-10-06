#!/usr/bin/env python
#-*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
from thyapi import handlers


from tornado.options import define, options
define('port', help='a port to handle traffic', type=int, default=8077)


def make_app():
    '''
    return application for test
    '''
    return tornado.web.Application(
        handlers=[
            (r'^/?$', handlers.IndexHandler),
        ],
        debug=True
    )

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = make_app()
    tornado.httpclient.AsyncHTTPClient.configure(
        "tornado.curl_httpclient.CurlAsyncHTTPClient")
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


#eof
