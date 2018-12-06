#!/usr/bin/python
#-*- coding:UTF-8 -*-
# __author__=sandy
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#创建项目对象
app=Flask(__name__)

app.config.from_object('blog.setting')#模块下的seting文件名，不用加后缀名
# app.config.from_envvar('FLASKR_SETTINGS')#环境变量，指向配置文件的路径
#创建数据库对象
db=SQLAlchemy(app)