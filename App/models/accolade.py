from .student import Student
from App.database import db

class Accolade(db.Model):
  accoladeId= db.Column(db.Integer, primary_key=True)
  studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
  award= db.Column(db.Integer)

  def __init__(self, recordId, studentId, award):
    self.accoladeId= recordId
    self.studentId= studentId
    self.hours= award

  def __repr__(self):
    return f'<Accolade {self.accoladeId} for student {self.student.username} due to having {self.award} hours logged in>'

  def createAccolade(studentId, award):
    try:
      student= Student.query.get(studentId)
    except NotFound as nf:
      print("Student not found")
    else:
      newAccolade= Accolade(studentId, award)
      return newAccolade
      
    
