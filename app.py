from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='main')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://davidgaither@localhost/school'

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name= db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)

class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(30))

class Teachers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name= db.Column(db.String(20))
    age = db.Column(db.Integer)
    subject = db.Column(db.Integer)


#GET - graabbing info
#PUT - updating info within db
#DELETE - deleting an entry within the db
#POST - creating an entry to the db


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api/v1/students/', methods=['GET'])
def get_all_students():
    students = Students.query.all()

    json_students = []
    for stud in students:
        subject = Subjects.query.get(stud.subject)
        subject_name = subject.subject
        
        teacher = Teachers.query.filter_by(subject=stud.subject).first()
        teacher_name = f"{teacher.first_name} {teacher.last_name}"
        
        student_data = {
            'id': stud.id,
            'first_name': stud.first_name,
            'last_name': stud.last_name,
            'age': stud.age,
            'class': {
                'subject': subject_name,
                'teacher': teacher_name
            }
        }
        json_students.append(student_data)
    
    response = jsonify(json_students)
    return response


@app.route('/api/v1/teachers/', methods=['GET'])
def get_all_teachers():
    teachers = Teachers.query.all()

    json_teachers = []
    for teach in teachers:
        subject = Subjects.query.get(teach.subject)
        subject_name = subject.subject

        students = Students.query.filter_by(subject=teach.subject).all()
        student_names = [f"{student.first_name} {student.last_name}" for student in students]

        teacher_data = {
            'first_name': teach.first_name,
            'last_name': teach.last_name,
            'age': teach.age,
            'subject': {
                'subject': subject_name,
                'students': student_names
            }
        }
        json_teachers.append(teacher_data)

    response = jsonify(json_teachers)
    return response


@app.route('/api/v1/subjects/', methods=['GET'])
def get_all_subjects():
    subjects = Subjects.query.all()

    json_subjects = []
    for subj in subjects:
        teacher = Teachers.query.filter_by(subject=subj.id).first()
        students = Students.query.filter_by(subject=subj.id).all()
        student_data = [f"{student.first_name} {student.last_name}" for student in students]

        subject_data = {
            'subject': subj.subject,
            'teacher': f"{teacher.first_name} {teacher.last_name}",
            'students': student_data
        }
        json_subjects.append(subject_data)

    response = jsonify(json_subjects)
    return response




app.run(port=8000, debug=True)