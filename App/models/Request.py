from App.database import db

class Request(db.Model):
   requestId= recordId = db.Column(db.Integer, primary_key=True)
   studentId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
   status = db.Column(db.String(30))#default=pending, approved, denied
   student = db.relationship("Student", backref=db.backref("requests", lazy=True))

   def __init__(self, studentId):
     self.studentId=studentId
     self.status="pending"

   def __repr__(self):
    return f'<Request no. {self.requestId} Student {self.student.username} Status: {self.status}>'

   def createRequest():
     newRequest= Request()
     db.session.add(newRequest)
     db.session.commit()
     return newRequest

   def approveRequest(selectedRequest):
     try:
        request = Request.query.filter_by(requestId = selectedRequest).first()
        if request is None:
           print("Request not found")
           return None
        request.status="approved"
        db.session.commit()
        return request
     except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None

   def denyRequest(selectedRequest):
     try:
        request = Request.query.filter_by(requestId = selectedRequest).first()
        if request is None:
           print("Request not found")
           return None
        request.status="denied"
        db.session.commit()
        return request
     except Exception as e:
        db.session.rollback()
        print("Error: ", e)
        return None
