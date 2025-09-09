#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#decorator-functions that take functions as arguments and return them decorated with new features.
@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

#views -functions that map to URLs.

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

if __name__== '__main__':
    app.run(port=5555, debug=True)