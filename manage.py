#!/usr/bin/env python
#coding=utf-8
'''
Created on 2016��10��19��

@author: huangning
'''
import os
from app import create_app, db
from app.models import User, Role,Post,Comment
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role,Post=Post,Comment=Comment)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
    #app.run()