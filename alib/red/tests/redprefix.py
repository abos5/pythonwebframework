#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
from unittest import TestCase
sys.path.append('/data/virtualenv/abstractframework/af/alib')
from red import redprefix


class FooTestCase(TestCase):

    def test_foo(self):
        self.assertEquals(1, 1)

    def test_bar(self):
        self.assertEquals(1, 2)

#eof
