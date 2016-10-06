#!/usr/bin/env python
#-*- coding: utf-8 -*-

from . import exceptions
__all__ = ['RedPrefix']


#
#
def build_connection(host, port=6379, password='', db=0):
    pass


connections = dict()


class RedPrefix(object):

    @property
    def connection(self):
        '''
        Writing as a property because it's called as a property.
        '''

        return connections[self.connectionIndex]

    @property
    def connectionIndex(self):
        '''should be able to be modified in an instance
        because of distributed usages.

        Writing as a property because it's called as a property.
        '''

        return 'default'

    def __getattr__(self, name):
        return getattr(self.connection, name)


#eof
