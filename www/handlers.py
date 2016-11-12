#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Dung'

' url handlers '

import re
import time
import json
import logging
import hashlib
import base64
import asyncio
from models import User
from models import Blog
from coroweb import get, post
from apis import Page

@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, adipisicing elit, sed do.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/api/users')
async def api_get_user(*, page='1'):
    page_index = get_page_index(page)
    num = await User.findNumber('count(id)')
    p = Page(num, page_index)
    if num == 0:
        return dict(page=p, users=())
    users = await User.findAll(orderBy='created_at desc', limit=(p.offset, p.limit))
    for u in  users:
        u.passwd = '******'
    return dict(page=p, users=users)

def get_page_index(page_str):
    p = 1
    try:
        p = int(page_str)
    except ValueError as e:
        pass
    if p < 1:
        p = 1
    return p