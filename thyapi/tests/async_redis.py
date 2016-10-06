#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#
import time
from tornado.testing import AsyncTestCase, gen_test
from tornado import gen
from tornado import ioloop
from tornado.stack_context import ExceptionStackContext
import tornadoredis


@gen.coroutine
def delay_async(seconds):
    yield gen.sleep(seconds)
    yield gen.sleep(seconds)


@gen.coroutine
def delay_async_cb(seconds, callback):
    yield gen.sleep(seconds)
    callback()


def delay(seconds):
    time.sleep(seconds)


class MyTestCase(AsyncTestCase):

    def no_test_delay(self):
        seconds = 0.5
        start = time.time()
        delay(seconds)
        duration = time.time() - start
        self.assertAlmostEqual(duration, seconds, places=2)

    def no_test_delay_async(self):
        start = time.time()
        io_loop = ioloop.IOLoop.instance()
        seconds = 0.5
        self.failure = None

        def done():
            duration = time.time() - start
            self.assertAlmostEqual(duration, 1, places=2)
            io_loop.stop()

        def handle_exception(type, value, tb):
            io_loop.stop()
            self.failure = value
            return True

        with ExceptionStackContext(handle_exception):
            delay_async(seconds, done)

        io_loop.start()
        if self.failure:
            raise self.failure

    def no_test_delay_async_test_wait(self):
        start = time.time()
        seconds = 0.5
        delay_async(seconds, self.stop)
        self.wait()
        duration = time.time() - start
        self.assertAlmostEqual(duration, 0.5, places=2)
        self.assertAlmostEqual(duration, 1, places=2)

    @gen_test
    def test_redis_lpush(self):
        start = time.time()
        c = tornadoredis.Client(host='python.i.abos.space')

        rs = yield gen.Task(
            c.lpush,
            'python:thyapi:tests:async_redis:awesome',
            1
        )
        # yield gen.Task(pipe.execute)
        # yield gen.Task(pipe.execute)
        self.assertEquals(1, rs)
        duration = time.time() - start
        self.assertAlmostEqual(duration, 0)

    @gen_test
    def no_test_delay_async_test_coroutine(self):
        start = time.time()
        seconds = 0.5
        yield gen.Task(delay_async, seconds)
        duration = time.time() - start
        # self.assertAlmostEqual(duration, 0.5, places=2)
        self.assertAlmostEqual(duration, 1, places=2)








# eof
