from .student import Student
from App.database imprort db

class Record(db.Model):
  recordId = db.Column(db.Integer, primary_key=True)
  studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
  hours= db.Column(db.Integer)

  def __init__(self, recordId, studentId, hours):
    self.recordId= recordId
    self.studentId= studentId
    self.hours= hours

  def __repr__(self):
    return f'<record {self.recordId} Student {self.student.username} Hours Logged: {self.hours}>'

  def updateRecord(self, hours):
    self.hours=hours
    return
