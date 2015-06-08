#!/usr/bin/env python3
from flask import Flask, render_template
from flask_wtf import Form
from wtforms.fields.html5 import DateField
app = Flask(__name__)
app.secret_key = 'coa7674c694607b169e57593a4952ea26fol!'

class Form(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')


@app.route('/', methods=['POST','GET'])
def hello_world():
    form = Form()
    if form.validate_on_submit():
        return form.dt.data.strftime('%Y-%m-%d')
    return render_template('audioArchiv.html', form=form)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)