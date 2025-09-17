from .user import User
from .accolade import Accolade
from .request import Request
from .record import Record
from App.database import db

class Student(User):
  __tablename__ = 'student'
  __mapper_args__ = {
      'polymorphic_identity': 'student',
    }

  def __init__(self, username, password):
      self.username = username
      self.set_password(password)
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
      record = Record.query.filer(Record.studentId == self.id).first()
      print(repr(record))
      return None
    elif search and search.status == "denied":
      print("Your request for hours has been denied.")
      return None
    else:
      request = Request()
      return request.createRequest(self.id)
    
