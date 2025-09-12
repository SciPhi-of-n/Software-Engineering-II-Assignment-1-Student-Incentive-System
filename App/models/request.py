from .student import Student
from .staff import Staff
from App.database imprort db

class Request(db.Model):
   __tablename__ = 'requests'
  requestId= recordId = db.Column(db.Integer, primary_key=True)
  studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
  staffId = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
  status = db.Column(db.String(30))#default=pending, approved, denied

  def __init__(self):
    self.status="pending"

  def __repr__(self):
    return f'<Request for Hours no. {self.requestId} Student {self.student.username} Staff: {self.staff.username} Status: {self.status}>'

  def createRequest(self, studentId):
    newRequest= Request()
    newRequest.studentId = studentId
    db.session.add(newRequest)
    db.session.commit()
    return newRequest

  def approveRequest(self, selectedRequest,  staffId):
    request = session.query(Request).filter_by(requestId = selectedRequest).first()
    try:
      request.staffId= staffId
      request.status="approved"
      db.session.commit(request)
      return request
    except:
      db.session.rollback()
      printf("Request not found")
      return none

  def denyRequest(self, selectedRequest,  staffId):
    request = session.query(Request).filter_by(requestId = selectedRequest).first()
    try:
      request.staffId= staffId
      request.status="denied"
      db.session.commit(request)
      return request
    except:
      db.session.rollback()
      printf("Request not found")
      return none
      
    
