import os
import subprocess
import getpass
from flask import Flask, request, render_template, url_for, send_from_directory

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def getIndex():
    return render_template('index.html')


@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route('/static/<path:path>')
def sendFile(path):
    return send_from_directory('static', path)

@app.route('/about')
def getabout():
    return render_template('about.html')

@app.route('/news')
def getnews():
    return render_template('news.html')


if __name__ == "__main__":
    app.run()
