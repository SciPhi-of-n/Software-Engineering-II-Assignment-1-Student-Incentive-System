from .user import User
from .Accolade import Accolade
from .Request import Request
from App.database import db

class Student(User):
  hours=db.Column(db.Integer)
  request = db.relationship('Request', backref=db.backref('requester', uselist=False))
  accolades = db.relationship('Accolade', backref=db.backref('awardee', lazy="joined"))
  __mapper_args__ = {
      'polymorphic_identity': 'student',
    }

  def __init__(self, username, password, hours=0):
      self.username = username
      self.set_password(password)
      self.hours=hours
      self.user_type = "student"
  
  def __repr__(self):
    return f'<ID {self.id} Student {self.username} Hours: {self.hours}>'

  def createStudent(username, password, hours):
    newStudent = Student(username, password, hours)
    try:
      db.session.add(newStudent)
      db.session.commit()
      return newStudent
    except:
      db.session.rollback()
      return None
        
  def getStudent(id):
    try:
      student = Student.query.get(id)
      if student == None:
        raise Exception(f"No student with the ID {id} could be found")
      return student
    except Exception as e:
      print(e)
      return None
    
  def getAllStudents():
    return Student.query.all()

  def viewAccolades(self):
    return Accolade.query.filter(Accolade.studentId == self.id).all()

  def requestHours(self):
    request = Request.createRequest(self.id)
    return request
    
