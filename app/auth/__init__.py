#coding=utf-8
'''
Created on 2016年10月20日

@author: huangning
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views