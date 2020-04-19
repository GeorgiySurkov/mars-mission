import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
from flask import Flask
import os

from .data.db_session import global_init

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or 'super_secret_key'
global_init(os.path.join(BASE_DIR, 'db', 'blogs.sqlite'))

from .routes import *
