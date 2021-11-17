from flask import Flask, redirect, url_for, render_template, request, jsonify, app,make_response
import json
import pdfkit
app = Flask(__name__)

class Page(object):

    def __init__(self):
        pass

    def home(self):
        # http://127.0.0.1:5000/calculate_exam_grade
        if request.method == 'POST':
                return redirect(url_for('second'))
        return render_template("index.html")


    def second(self):
        if request.method == 'POST':
            Photo = request.form['Photo']
            fname = request.form['fname']
            lname = request.form['lname']
            birthday = request.form['birthday']
            email = request.form['email']
            address = request.form['address']
            DriverLicence = request.form['DriverLicence']
            AboutMe = request.form['AboutMe']
            Education = request.form['Education']
            Experience = request.form['Experience']
            Skills = request.form['Skills']
            Hobbies = request.form['Hobbies']
            Language1 = request.form['Language1']
            Language2 = request.form['Language2']
            Language3 = request.form['Language3']
            Language4 = request.form['Language4']
            return redirect(url_for('pdfCV'))
        return render_template('second.html')

    def pdf_generate(self):
        render = render_template("pdf_template.html")
        pdf = pdfkit.from_string(render, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline;filename=output.pdf'
        return response