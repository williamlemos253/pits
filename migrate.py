#coding: UTF-8
import os
from os import environ
from pits import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from pits import *


app = Flask(__name__)
app.config.from_object('pits.config')

if __name__ == '__main__':
    manager.run()