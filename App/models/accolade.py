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
    return f'<Accolade awarded to student {self.studentId} for to having {self.award} hours logged in>'

  def createAccolade(studentId, award):
    try:
      student= Student.query.get(studentId)
      if student is None:
        print("Student not found")
        return None
      newAccolade= Accolade(studentId, award)
      db.session.add(newAccolade)
      db.session.commit()
      return newAccolade
    except Exception as e:
      db.session.rollback()
      print("Error: ", e)
      return None
      
    
