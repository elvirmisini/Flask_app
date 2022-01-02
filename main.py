from flask import Flask, redirect, url_for, render_template, request, jsonify, app, make_response
import json
import pdfkit as pdf
from pages import Page
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Page=Page()

@app.route("/",methods = ['POST', 'GET'])
def hello():

    return Page.home()

@app.route("/second",methods = ['POST', 'GET'])
def second():

    return Page.second()

@app.route("/third",methods = ['POST', 'GET'])
def third():

    return Page.third()

@app.route("/about",methods = ['POST', 'GET'])
def about():

    return Page.about()

@app.route("/pdfCV",methods = ['POST', 'GET'])
def pdf_template():

    return Page.pdf_generate()

@app.route("/pdfCoverLetter",methods = ['POST', 'GET'])
def pdf_coverLetter_template():

    return Page.pdf_coverLetter_template()

if __name__ == '__main__':
    app.run(debug=True)


