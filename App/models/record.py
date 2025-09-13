from .student import Student
from App.database imprort db

class Record(db.Model):
  recordId = db.Column(db.Integer, primary_key=True)
  studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False, unique=True)
  hours= db.Column(db.Integer)
  student = db.relationship('Student', backref=db.backref('record', uselist=False))

  def __init__(self, recordId, studentId, hours):
    self.recordId= recordId
    self.studentId= studentId
    self.hours= hours

  def __repr__(self):
    return f'<Student {self.student.username} Hours Logged: {self.hours}>'

  def createRecord(self):
    try:
      db.session.add(self)
      db.session.commit()
      return self
    except IntegrityError as e:
      db.session.rollback()
      printf("There can only be one record per student.")
      return None

  def updateRecord(studentId, hours):
    studentFound= Student.query.filter_by(id = studentName).first()
    if not studentFound:
      printf("No student of the name {studentName} could be found")
      return None 
    record = Record.query.filter_by(studentId = studentFound.id).first()
    if not record:
      printf("{studentName} has no record")
      return None
    try:
      record.hours=hours
      db.session.commit()
      printf("Record Updated")
      return record
    except Expection as e:
      db.session.rollback()
      print("Error: ", e)
      return None
