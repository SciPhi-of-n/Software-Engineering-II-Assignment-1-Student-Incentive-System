from .user import User
from App.database import db

class Student(User):
  __tablename__ = 'student'
  __mapper_args__ = {
      'polymorphic_identity': 'student',
    }

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = "student" 
