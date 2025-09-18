from .user import User
from .Student import Student
from .Request import Request
from App.database import db

class Staff(User):
  __mapper_args__ = {
      'polymorphic_identity': 'staff',
    }

  def __init__(self, username, password):
    self.username = username
    self.set_password(password)
    self.user_type = "staff"

  def __repr__(self):
    return f'<Staff {self.username}>'

  def logHours(studentId, hours):
    student = Student.query.get(studentId)
    if student:
      student.hours = hours
      db.session.commit()
      return True
    return False
  
  def viewRequests():
    requests = Request.query.all()
    return requests

  def approveRequest(requestId, self):
    return Request.approveRequest(requestId, self.id)
  
  def denyRequest(requestId, self):
    return Request.denyRequest(requestId, self.id)