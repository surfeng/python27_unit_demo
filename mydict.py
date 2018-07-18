#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/7/18 11:39
# @Author : 
# @File : mydict.py
# @Software: PyCharm
# @Desc  :

class Dict(dict):

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value