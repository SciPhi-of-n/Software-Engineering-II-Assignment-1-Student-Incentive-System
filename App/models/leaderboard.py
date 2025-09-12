from .student import Student
from App.database imprort db

class Leaderboard(db.Model):
  studentId = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
  students = db.relationship('Student', backref=db.backref('leaderboard', lazy='joined'))
  records = db.relationship('Record', backref=db.backref('leaderboard', lazy='joined'))

  def __int__(self, studentId):
    self.studentId=studentId

