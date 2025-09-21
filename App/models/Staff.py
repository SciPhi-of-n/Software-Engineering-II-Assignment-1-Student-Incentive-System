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

  def createStaff(username, password):
    newStaff = Staff(username, password)
    try:
      db.session.add(newStaff)
      db.session.commit()
      return newStaff
    except:
      db.session.rollback()
      return None
        
  def getStaff(id):
    from App.models.Staff import Staff
    try:
      staff = Staff.query.get(id)
      if staff == None:
        raise Exception(f"No member of staff with the ID {id} could be found")
      return staff
    except Exception as e:
      print(e)
      return None
        
  def getAllStaff():
    return Staff.query.all()

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