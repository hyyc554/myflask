#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : app.py.py
@version   : 1.0
@Time      : 2019/3/17 19:59
Description about this file:

"""
from flask import Flask
app  = Flask(__name__)

@app.route("/")
def index():
    return "<h1>hello flask</h1>"


