from .student import Student
from .staff import Staff
from App.database import db

class Request(db.Model):
   __tablename__ = 'requests'
   requestId= recordId = db.Column(db.Integer, primary_key=True)
   studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
   staffId = db.Column(db.Integer, db.ForeignKey('staff.id'), nullable=False)
   status = db.Column(db.String(30))#default=pending, approved, denied
   student= db.relationship('Student', backref=db.backref('requests', uselist=False))
   staff= db.relationship('Student', backref=db.backref('handled_request', lazy='joined'))

   def __init__(self, studentId):
     self.studentId=studentId
     self.staffId=None
     self.status="pending"

   def __repr__(self):
    return f'<Request for Hours no. {self.requestId} Student {self.student.username} Staff: {self.staff.username} Status: {self.status}>'

   def createRequest(studentId):
     newRequest= Request()
     newRequest.studentId = studentId
     db.session.add(newRequest)
     db.session.commit()
     return newRequest

   def approveRequest(selectedRequest, staffId):
     try:
        request = Request.query.filter_by(requestId = selectedRequest).first()
        if request is None:
           print("Request not found")
           return None
           
        request.staffId= staffId
        request.status="approved"
        db.session.commit()
        return request
     except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None

   def denyRequest(selectedRequest, staffId):
     try:
        request = Request.query.filter_by(requestId = selectedRequest).first()
        if request is None:
           print("Request not found")
           return None
           
        request.staffId= staffId
        request.status="denied"
        db.session.commit()
        return request
     except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
