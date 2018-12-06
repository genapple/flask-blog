#!/usr/bin/python
#-*- coding:UTF-8 -*-
# __author__=sandy
from blog import db
class User(db.Model):
    __tablename__=='b_user'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(10),unique=True)