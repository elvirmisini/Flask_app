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
        return render_template('second.html')

    def pdf_generate(self):
        Photo = request.form.get('Photo')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        birthday = request.form.get('birthday')
        email = request.form.get('email')
        address = request.form.get('address')
        DriverLicence = request.form.get('DriverLicence')
        AboutMe = request.form.get('AboutMe')
        Education = request.form.get('Education')
        Experience = request.form.get('Experience')
        Skills = request.form.get('Skills')
        Hobbies = request.form.get('Hobbies')
        Language1 = request.form.get('Language1')
        Language2 = request.form.get('Language2')
        Language3 = request.form.get('Language3')
        Language4 = request.form.get('Language4')
        levelL1=request.form.get('levelL1')
        levelL2=request.form.get('levelL2')
        levelL3=request.form.get('levelL3')
        levelL4=request.form.get('levelL4')
        # return render_template("pdf_template.html",Photo=Photo,fname=fname,lname=lname,birthday=birthday,email=email,address=address,DriverLicence=DriverLicence,AboutMe=AboutMe,Education=Education,Experience=Experience,Skills=Skills,Hobbies=Hobbies,Language1=Language1,Language2=Language2,Language3=Language3,Language4=Language4,levelL1=levelL1,levelL2=levelL2,levelL3=levelL3,levelL4=levelL4)
        render = render_template("pdf_template.html",Photo=Photo,fname=fname,lname=lname,birthday=birthday,email=email,address=address,DriverLicence=DriverLicence,AboutMe=AboutMe,Education=Education,Experience=Experience,Skills=Skills,Hobbies=Hobbies,Language1=Language1,Language2=Language2,Language3=Language3,Language4=Language4,levelL1=levelL1,levelL2=levelL2,levelL3=levelL3,levelL4=levelL4)
        pdf = pdfkit.from_string(render, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline;filename=CV of '+fname+lname+'.pdf'
        return response