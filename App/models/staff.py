from .user import User
from .student import Student
from .request import Request
from App.database import db

class Staff(User):
  __mapper_args__ = {
      'polymorphic_identity': 'staff',
    }

  def __init__(self, username, password):
    self.username = username
    self.set_password(password)
    self.user_type = "staff"

  def logHours(studentId, hours):
    student= Student.query.get(studentId)
    if not student:
      print("No student could be found")
      return None
    try:
      student.hours = hours
      db.session.commit()
      return print("Student Hours Updated.")
    except Exception as e:
      db.session.rollback()
      return print("Error updating hours: {e}")
  
  def viewRequests():
    requests = Request.query.all()
    print(repr(requests))

  def approveRequest(requestId, self):
    return Request.approveRequest(requestId, self.id)
  
  def denyRequest(requestId, self):
    return Request.denyRequest(requestId, self.id)