from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    body = db.Column(db.String(200))  
    # 将index设为True来开启索引，并使用default参数设置了字段默认值，timestamp字段的默认值是datetime.utcnow而不是datetime.utcnow()。前者是可调用的函数/方法对象（即名称），而后者是函数/方法调用（即动作）
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)