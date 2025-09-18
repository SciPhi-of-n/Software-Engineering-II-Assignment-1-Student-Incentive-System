from .user import User
from .accolade import Accolade
from .request import Request
from App.database import db

class Student(User):
  hours=db.Column(db.Integer)
  request = db.relationship('Request', backref=db.backref('student', uselist=False))
  accolade = db.relationship('Accolade', backref=db.backref('student', uselist=False))
  __mapper_args__ = {
      'polymorphic_identity': 'student',
    }

  def __init__(self, username, password, hours):
      self.username = username
      self.set_password(password)
      self.hours=hours
      self.user_type = "student"

  def viewAccolades(self):
    return Accolade.query.filter(Accolade.studentId == self.id).all()

  def requestHours(self):
    search = Request.query.filter(Request.studentId == self.id).all()
    if search and search.status == "pending":
      print("Your request is still being processed. Please wait.")
      return None
    if search and search.status == "approved":
      print("Your request for hours has been approved")
      return None
    elif search and search.status == "denied":
      print("Your request for hours has been denied.")
      return None
    else:
      request = Request()
      return request.createRequest(self.id)
    
  def viewHours(self):
    print("Hours Logged: {self.hours}")