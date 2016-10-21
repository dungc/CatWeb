#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Dung'

' url handlers '

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }