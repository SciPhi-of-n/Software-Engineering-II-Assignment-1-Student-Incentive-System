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
    if search:
      db.session.rollback()
      printf("Only one request can be made per student")
      return none
    else:
      request = Request()
      return request.createRequest(self.id)
    
