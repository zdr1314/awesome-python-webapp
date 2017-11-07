#!usr/bin/env python
# _*_ coding: utf-8 _*_
import threading

class _Engine(object):
    def __init__(self, connect):
        self._connect = connect

    def connect(self):
        return self._connect()
engine = None
class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transaction = 0

    def is_init(self):
        return not self.connection is None