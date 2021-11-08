from flask import Flask, redirect, url_for, render_template, request, jsonify, app
import json
app = Flask(__name__)

class Page(object):

    def __init__(self):
        pass

    def home(self):
        # http://127.0.0.1:5000/calculate_exam_grade
        if request.method == 'POST':
                return render_template('second.html')
        return render_template("index.html")


    def second(self):
        if request.method == 'POST':
            return render_template('index.html')
        return render_template("second.html")
