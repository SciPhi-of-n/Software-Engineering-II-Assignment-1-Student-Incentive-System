from .student import Student
from App.database import db

class Leaderboard(db.Model):
  def getLeaderboard():
    return (db.session.query(Student).order_by(Student.hours.desc()).all())

  def displayLeaderboard():
    leaderboard = Leaderboard.getLeaderboard()
    print("Leaderboard")
    rank=0
    score=None
    for student in leaderboard:
      if student.hours is not score:
        rank=rank+1
      print("{rank}. {student.name} {student.hours}")
      score = student.hours
      
