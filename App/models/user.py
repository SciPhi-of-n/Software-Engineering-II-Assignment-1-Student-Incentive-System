from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    user_type =  db.Column(db.String(120), nullable=False)
    __mapper_args__ = {'polymorphic_identity': 'user', 'polymorphic_on': user_type}

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def createStudent(username, password, hours):
        from App.models.Student import Student
        newStudent = Student(username, password, hours)
        try:
            db.session.add(newStudent)
            db.session.commit()
            return newStudent
        except:
            db.session.rollback()
            return None
        
    def getStudent(id):
        try:
            from App.models.Student import Student
            student = Student.query.get(id)
            if student == None:
                raise Exception(f"No student with the ID {id} could be found")
            return student
        except Exception as e:
            print(e)
            return None
    
    def getAllStudents():
        from App.models.Student import Student
        return Student.query.all()

    def createStaff(username, password):
        from App.models.Staff import Staff
        newStaff = Staff(username, password)
        try:
            db.session.add(newStaff)
            db.session.commit()
            return newStaff
        except:
            db.session.rollback()
            return None
        
    def getStaff(id):
        from App.models.Staff import Staff
        try:
            staff = Staff.query.get(id)
            if staff == None:
                raise Exception(f"No member of staff with the ID {id} could be found")
            return staff
        except Exception as e:
            print(e)
            return None
        
    def getAllStaff():
        from App.models.Staff import Staff
        return Staff.query.all()