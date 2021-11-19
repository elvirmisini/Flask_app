from flask import Flask, redirect, url_for, render_template, request, jsonify, app, make_response
import json
import pdfkit
from pages import Page
import os

app = Flask(__name__)

Page=Page()

@app.route("/",methods = ['POST', 'GET'])
def hello():

    return Page.home()

@app.route("/second",methods = ['POST', 'GET'])
def second():

    return Page.second()

@app.route("/pdfCV",methods = ['POST', 'GET'])
def pdf_template():

    return Page.pdf_generate()

if __name__ == '__main__':
    app.run(debug=True)


