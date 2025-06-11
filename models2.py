from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/students'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Students (db.Model):
    __tablename__ = "Students"
    school_id = db.Column (db.Integer , primary_key= True)
    national_id = db.Column (db.Integer)
    first_name = db.Column (db.String(100))
    last_name = db.Column (db.String(100))
    course_name = db.Column (db.String(1000))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    

#with app.app_context():
        #student = Students.query.all()
        #for s in student:
           #print(f"School ID: {s.school_id}, National ID: {s.national_id}, "
             # f"Name: {s.first_name} {s.last_name}, Course: {s.course_name}, Email: {s.}")

   

#print("\n Enter student details:")
#school_id = int(input("School ID: "))
#national_id = int(input("National ID: "))
#first_name = input("First Name: ")
#last_name = input("Last Name: ")
#course_name = input("Course Name: ")


