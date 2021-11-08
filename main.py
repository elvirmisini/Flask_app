from flask import Flask, redirect, url_for, render_template, request, jsonify, app
import json
from pages import Page

app = Flask(__name__)

Page=Page()

@app.route("/",methods = ['POST', 'GET'])
def hello():

    return Page.home()

@app.route("/second",methods = ['POST', 'GET'])
def second():

    return Page.second()

if __name__ == '__main__':
    app.run(debug=True)


