#coding=utf-8
'''
Created on 2016��10��19��

@author: huangning
'''
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views, errors