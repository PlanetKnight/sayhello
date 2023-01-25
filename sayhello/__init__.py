# pip install flask
# pip install python-dotenv
# pip install flask-sqlalchemy
# pip install flask-wtf
# pip install bootstrap-flask
# pip install flask-moment
# pip install faker
# pip install flask-debugtoolbar
# pip freeze > requirements.txt
# pip install -r requirements.txt

"""say hello to the world"""
# module docstring
# import mysayhello
# mysayhello.__doc__

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap4
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

app = Flask('sayhello')
# 在创建程序实例后，使用config对象的from_pyfile()方法即可加载配置，传入配置模块的文件名作为参数
app.config.from_pyfile('settings.py')
# 前者用来删除Jinja2语句后的第一个空行，后者则用来删除Jinja2语句所在行之前的空格和制表符
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap4(app)
moment = Moment(app)
# toolbar = DebugToolbarExtension(app)

from sayhello import views, errors, commands