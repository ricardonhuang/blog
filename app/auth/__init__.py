#coding=utf-8
'''
Created on 2016��10��20��

@author: huangning
'''
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views