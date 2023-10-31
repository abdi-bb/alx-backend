#!/usr/bin/env python3
'''
Module: '0-app'
Basic Flask App
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)
