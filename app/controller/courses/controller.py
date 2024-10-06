from flask import render_template, redirect, request, url_for, jsonify
from . import course
import app.models.course as CourseModel
import app.models.college as CollegeModel
from app.controller.courses.forms import CourseForm 

@course.route("/course")
def index():
    keyword = request.args.get('keyword', default='', type=str)
    courses = CourseModel.Courses.all(keyword)

    return render_template("course/index.html", courses=courses)

@course.route('/course/create', methods=['POST', 'GET'])
def create():
    form = CourseForm(request.form)
    
    if request.method == 'POST' and form.validate():
        course = CourseModel.Courses(code=form.name.data, name=form.code.data, college_id=form.college_id.data)
        course.add()

        return redirect('/course')
    else:
        colleges = CollegeModel.Colleges.all('')

        return render_template("course/create.html", form=form, data=colleges)
    
@course.route('/course/edit/<id>', methods=['GET'])
def edit(id):
    course = CourseModel.Courses.edit(id)
    colleges = CollegeModel.Colleges.all('')

    return render_template('course/edit.html', data=course, datas=colleges)

@course.route('/course/<id>', methods=['POST'])
def update(id):
    if request.method == 'POST':
        code = request.form['code']
        name = request.form['name']
        college_id = request.form['college_id']
        CourseModel.Courses.update(id, code, name, college_id)

        return redirect(url_for('.index'))

@course.route('/course/delete', methods=['POST'])
def delete():
    id = request.form['id']

    if id:
        try:
            CourseModel.Courses.delete(id)
            
            return jsonify(success=True, message="Successful")
        except:
            return jsonify(success=False, message="Course is referenced in Students table")

    return jsonify(success=False, message="Failed")
