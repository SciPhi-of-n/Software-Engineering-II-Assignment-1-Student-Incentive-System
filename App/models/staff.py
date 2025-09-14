from .user import User
from App.database import db

class Staff(User):
  __mapper_args__ = {
      'polymorphic_identity': 'staff',
    }

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
        self.user_type = "staff"
