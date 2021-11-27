from flask import Flask, redirect, url_for, render_template, request, jsonify, app,make_response,flash
import json
import os
import pdfkit
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
class Page(object):

    def __init__(self):
        pass

    def home(self):
        # http://127.0.0.1:5000/calculate_exam_grade
        if request.method == 'POST':
                return redirect(url_for('second'))
        return render_template("index.html")

    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def second(self):
        return render_template('second.html')

    def third(self):
        return render_template('third.html')

    def about(self):
        return render_template('about.html')

    def pdf_generate(self):
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

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

                full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                return render_template("pdf_template.html",user_image=full_filename,fname=fname,lname=lname,birthday=birthday,email=email,address=address,DriverLicence=DriverLicence,AboutMe=AboutMe,Education=Education,Experience=Experience,Skills=Skills,Hobbies=Hobbies,Language1=Language1,Language2=Language2,Language3=Language3,Language4=Language4,levelL1=levelL1,levelL2=levelL2,levelL3=levelL3,levelL4=levelL4)
                # render = render_template("pdf_template.html",display_image=full_filename,fname=fname,lname=lname,birthday=birthday,email=email,address=address,DriverLicence=DriverLicence,AboutMe=AboutMe,Education=Education,Experience=Experience,Skills=Skills,Hobbies=Hobbies,Language1=Language1,Language2=Language2,Language3=Language3,Language4=Language4,levelL1=levelL1,levelL2=levelL2,levelL3=levelL3,levelL4=levelL4)
                pdf = pdfkit.from_string(render, False)
                response = make_response(pdf)
                response.headers['Content-Type'] = 'application/pdf'
                response.headers['Content-Disposition'] = 'inline;filename=CV of '+fname+lname+'.pdf'
                return response
    def pdf_coverLetter_template(self):
                fname = request.form.get('fname')
                lname = request.form.get('lname')
                TodayDate = request.form.get('TodayDate')
                email = request.form.get('email')
                address = request.form.get('address')
                Title = request.form.get('Title')
                AboutMe = request.form.get('AboutMe')
                levelL4 = request.form.get('levelL4')

                full_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                return render_template("pdf_template.html",  fname=fname, lname=lname,email=email, address=address,AboutMe=AboutMe,)
                # render = render_template("pdf_template.html",display_image=full_filename,fname=fname,lname=lname,birthday=birthday,email=email,address=address,DriverLicence=DriverLicence,AboutMe=AboutMe,Education=Education,Experience=Experience,Skills=Skills,Hobbies=Hobbies,Language1=Language1,Language2=Language2,Language3=Language3,Language4=Language4,levelL1=levelL1,levelL2=levelL2,levelL3=levelL3,levelL4=levelL4)
                pdf = pdfkit.from_string(render, False)
                response = make_response(pdf)
                response.headers['Content-Type'] = 'application/pdf'
                response.headers['Content-Disposition'] = 'inline;filename=CV of ' + fname + lname + '.pdf'
                return response