import os

port = int(os.environ.get('PORT', 5000))

app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, render_template, redirect, url_for
from flask_restful import Resource, Api, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

# Define the routes and their corresponding names
routes = [
        ("/about", "ABOUT"),
        ("/news", "NEWS"),
        ("/calendar", "CALENDAR"),
        ("/resources", "RESOURCES"),
        ("/contact", "CONTACT"),
]

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/news")
def news():
    return render_template("news.html")

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")

@app.route("/resources")
def resources():
    return render_template("resources.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/")
def home():
    return redirect(url_for("about"))

if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
