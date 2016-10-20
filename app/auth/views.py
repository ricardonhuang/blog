#coding=utf-8
'''
Created on 2016��10��20��

@author: huangning
'''
from flask import render_template
from . import auth


@auth.route('/login')
def login():
    return render_template('auth/login.html')