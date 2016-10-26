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
from coroweb import get, post

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }