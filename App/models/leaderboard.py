from .student import Student
from .record import Record
from App.database import db

class Leaderboard(db.Model):
  students = db.relationship('Student', backref=db.backref('leaderboard', lazy='joined'))
  records = db.relationship('Record', backref=db.backref('leaderboard', lazy='joined'))

  def getLeaderboard():
    return (db.session.query(Student, Record).join(Record, Student.id == Record.studentId).order_by(Record.hours.desc()).all())

  def displayLeaderboard():
    leaderboard = Leaderboard.getLeaderboard()
    print("Leaderboard")
    rank=1
    for student, record in leaderboard:
      print("{rank}. {student.name}")
      rank=rank+1
