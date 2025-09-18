from .Student import Student
from App.database import db

class Accolade(db.Model):
  accoladeId= db.Column(db.Integer, primary_key=True)
  studentId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  award = db.Column(db.String(100))

  def __init__(self, studentId, award):
    self.studentId= studentId
    self.award= award

  def __repr__(self):
    return f'<Accolade no. {self.accoladeId} Student {self.student.username} Award: {self.award}>'

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