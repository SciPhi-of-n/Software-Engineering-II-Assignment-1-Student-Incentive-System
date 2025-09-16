from .user import User
from .record import Record
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
    return Record.updateRecord(studentId, hours)
  
  def viewRequests():
    requests = Request.query.all()
    print(requests.__repr__())

  def approveRequest(requestId, self):
    return Request.approveRequest(requestId, self.id)
  
  def denyRequest(requestId, self):
    return Request.denyRequest(requestId, self.id)