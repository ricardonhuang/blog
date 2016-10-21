#coding=utf-8
'''
Created on 2016��10��19��

@author: huangning
'''
from flask import render_template
from . import main


@main.route('/')
def index():
    return render_template('index.html')
        