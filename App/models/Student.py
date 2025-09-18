from .user import User
from .Accolade import Accolade
from .Request import Request
from App.database import db

class Student(User):
  hours=db.Column(db.Integer)
  request = db.relationship('Request', backref=db.backref('student', uselist=False))
  accolade = db.relationship('Accolade', backref=db.backref('student', lazy="joined"))
  __mapper_args__ = {
      'polymorphic_identity': 'student',
    }

  def __init__(self, username, password, hours):
      self.username = username
      self.set_password(password)
      self.hours=hours
      self.user_type = "student"
  
  def __repr__(self):
    return f'<Student {self.username} Hours: {self.hours}>'

  def viewAccolades(self):
    return Accolade.query.filter(Accolade.studentId == self.id).all()

  def requestHours(self):
    return Request.query.filter(Request.studentId == self.id).all()
    
  def viewHours(self):
    return self.hours