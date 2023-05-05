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

#landing page
@app.route('/')
@app.route('/start')
def start():
    return render_template('landingpage.html')

#search
@app.route("/search", methods=['POST','GET'])
def search():
    if request.method == 'POST':
        print('submit called post')
        default = '0'
        name = request.form.get('name',default)
        email = request.form.get('email',default)
        phone = request.form.get('phone',default)
        net_worth = request.form.get('net_worth',default)
        user_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'net_worth': net_worth
        }
        print(name,email,phone,net_worth)
        with open('data.json', 'a') as f:
            json.dump(user_data, f)
        return render_template("submit.html",name = name, net_worth = int(net_worth))


#runs the server on aux1
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224,debug=True)
