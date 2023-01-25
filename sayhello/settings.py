import os
import sys

from sayhello import app

# sys.platform 'linux' 'win32'
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# app.root_path存储程序实例所在路径 '/home/notebook/code/mysayhello/mysayhello'
# os.path.dirname(app.root_path)获取上层目录 '/home/notebook/code/mysayhello'
dev_db = prefix + os.path.join(os.path.dirname(app.root_path), 'data.db')

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db)
