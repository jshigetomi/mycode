#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import json

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

class UserForm(FlaskForm):
    name = StringField('name')
    email = StringField('email')
    phone = StringField('phone')
    net_worth = StringField('net_worth')
    submit = SubmitField('submit')

#landing page
@app.route("/", methods=['POST'])
@app.route("/start")
def start():
    form = UserForm()

    if request.method == 'POST':
        print('submit called get')
        name = form.name.data
        email = form.email.data
        phone = form.phone.data
        net_worth = form.phone.data
        user_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'net_worth': net_worth
        }
        with open('data.json', 'w') as f:
            json.dump(user_data, f)

    return render_template('landingpage.html',form=form)



#runs the server on aux1
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
