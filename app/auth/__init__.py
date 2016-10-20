#coding=utf-8
'''
Created on 2016Äê10ÔÂ20ÈÕ

@author: huangning
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views