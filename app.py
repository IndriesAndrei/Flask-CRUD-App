from flask import Flask, request, redirect, url_for, render_template
from flask_modus import Modus # to override methods like POST and GET

from student import Student


app = Flask(__name__)
modus = Modus(app)

students = []

@app.route('/')
def root():
    return redirect(url_for('index'))

@app.route('/students', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # we get the request inputed by user and get the name="first_name" 
        # and name="last_name" from the form
        new_student = Student(request.form['first_name'], request.form['last_name'])
        students.append(new_student)
        return redirect(url_for('index'))
    return render_template('index.html', students=students)

@app.route('/students/new')
def new():
    return render_template('new.html')

@app.route('/students/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def show(id):
   
    for student in students:
        if student.id == id:
            found_student = student
    # we can type also as : 
    # found_student = [student for student in students if student.id == id][0]
    if request.method == b'PATCH':
        found_student.first_name = request.form['first_name']
        found_student.last_name = request.form['last_name']
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        students.remove(found_student)
        return redirect(url_for('index'))
    return render_template('show.html', student=found_student)

@app.route('/students/<int:id>/edit')
def edit(id):
    for student in students:
        if student.id == id:
            found_student = student
    return render_template('edit.html', student=found_student)

if __name__ == '__main__':
    app.run(debug=True)