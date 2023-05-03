#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

#landing page
@app.route("/")
@app.route("/start")
def start():
    return render_template("landingpage.html")
#form submission
@app.route("/submit", methods = ["POST"])
def submit():
    if request.method == "POST":
        if request.form.get("nm"):



#runs the server on aux1
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
