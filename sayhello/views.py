from flask import flash, redirect, url_for, render_template

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message

@app.route('/', methods=['GET', 'POST'])
def index(): 
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        return redirect(url_for('index'))
    
    # 在获取message记录时，我们使用order_by()过滤器对数据库记录进行排序，参数是排序的规则。我们根据Message模型的timestamp字段值排序，字段上附加的排序方法为desc()，代表降序(descending)，同样还有一个asc()方法表示升序(ascending)
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html', form=form, messages=messages)