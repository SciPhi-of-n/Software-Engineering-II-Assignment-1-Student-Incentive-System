import click, pytest, sys
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User, Student, Staff, Request, Accolade
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users)


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    db.drop_all()
    db.create_all()
    student1=Student(username="Alice", password="alicepass", hours=15)
    student2=Student(username="Bob", password="bobpass", hours=35)
    student3=Student(username="Charlie", password="charliepass", hours=7)
    staff=Staff(username="Admin", password="adminpass")
    db.session.add(student1)
    db.session.add(student2)
    db.session.add(student3)
    db.session.add(staff)
    db.session.commit()
    print('database intialized')

@app.cli.command("leaderboard", help="Displays leaderboard")
def displayLeaderboardCommand():
    leaderboard=(db.session.query(Student).order_by(Student.hours.desc()).all())
    print("Leaderboard")
    rank=0
    score=None
    for student in leaderboard:
      if student.hours is not score:
        rank=rank+1
      print(f"{rank}. {student.username} {student.hours}")
      score = student.hours

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Student Commands
'''

student_cli = AppGroup('student', help='Student object commands')

@student_cli.command("create", help="Creates a student")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def createStudentCommand(username, password):
    student = Student(username, password)
    db.session.add(student)
    db.session.commit()
    print(f"Student {username} created")

@student_cli.command("list", help="Lists students in the database")
@click.argument("format", default="string")
def listStudentsCommand(format):
    students = Student.query.all()
    for student in students:
        print(repr(student))

@student_cli.command("request", help="Requests confirmation of hours")
@click.argument("studentid", default=1)
def requestHoursCommand(studentid):
    student = Student.query.get(studentid)
    if student:
        request = Request.createRequest(studentid)
        print("Request created")
    else:
        print("Student could not be found")

@student_cli.command("status", help="Displays the status of a request sent")
@click.argument("studentid", default=1)
def requestStatusCommand(studentid):
    student = Student.query.get(studentid)
    if student:
        requests = Request.query.filter(Request.studentId == studentid).all()
        if requests:
            for request in requests:
                if(request.status) == "pending":
                    print(f"Request {request.requestId} is current pending. Please wait.")
                else:
                    print(f"Request {request.requestId} has been {request.status}.")
        else:
            print("No requests were made by this student")
    else:
        print("Student could not be found")

@student_cli.command("accolades", help="Displays accolades of student")
@click.argument("studentid", default=1)
def requestHoursCommand(studentid):
    student = Student.query.get(studentid)
    if student:
        accolades = student.viewAccolades()
        if accolades:
            for accolade in accolades:
                print(repr(accolade))
        else:
            print("No accolades were earned")
    else:
        print("Student could not be found")

@student_cli.command("hours", help="Displays the hours of a student")
@click.argument("studentid", default=1)
def requestHoursCommand(studentid):
    student = Student.query.get(studentid)
    if student:
        print(f"Student {student.username} has earned {student.viewHours()} hours")
    else:
        print("Student could not be found")

app.cli.add_command(student_cli)

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)