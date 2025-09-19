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

  def respondRequest(requestId, status):
    if status == "approved":
      request = Request.approveRequest(requestId)
      if request:
        return True
    elif status == "denied":
      request = Request.denyRequest(requestId)
      if request:
        return True
    return False