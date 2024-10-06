from flask import render_template, redirect, request, url_for, jsonify
from . import student
import app.models.student as StudentModel
import app.models.course as CourseModel
from app.controller.students.forms import StudentForm 
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

@student.route("/")
@student.route("/student")
def index():
    keyword = request.args.get('keyword', default='', type=str)
    students = StudentModel.Students.all(keyword)

    return render_template("student/index.html", students=students)

@student.route("/student/create", methods=['POST', 'GET'])
def create():
    form = StudentForm(request.form)

    if request.method == 'POST':
        avatar_file = upload(request.files['avatar_file'])        
        url, options = cloudinary_url(avatar_file['public_id'], width=100, height=150, crop="fill")
        student = StudentModel.Students(avatar_url=url, id_number=form.id_number.data, first_name=form.first_name.data, last_name=form.last_name.data, course_id=form.course_id.data, year=form.year.data, gender=form.gender.data)
        student.add()

        return redirect(url_for('.index'))
    else:    
        courses = CourseModel.Courses.all('')

        return render_template("student/create.html", form=form, courses=courses)

@student.route("/student/edit/<id>", methods=['POST', 'GET'])
def edit(id):
    student = StudentModel.Students.edit(id)
    course = CourseModel.Courses.all('')

    return render_template("student/edit.html", data=student, datas=course)

@student.route('/student/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        avatar_file = request.files.get('avatar_file')
        current_student = StudentModel.Students.get_by_id(id)[0]
        
        if avatar_file:
            uploaded_avatar = upload(avatar_file)
            url, options = cloudinary_url(uploaded_avatar['public_id'], width=100, height=150, crop="fill")
            avatar_url = url
        else:
            avatar_url = current_student

        id_number = request.form['id_number']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        course_id = request.form['course_id']
        year = request.form['year']
        gender = request.form['gender']

        StudentModel.Students.update(id, avatar_url, id_number, first_name, last_name, course_id, year, gender)
        return redirect(url_for('.index'))
    else:
        return "Form validation failed", 400  

@student.route('/student/delete', methods=['POST'])
def delete():
    id = request.form['id']

    if id:
        StudentModel.Students.delete(id)

        return jsonify(success=True, message="Successful")

    return jsonify(success=False, message="Failed")
