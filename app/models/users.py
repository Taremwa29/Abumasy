from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), nullable=False)
    power = db.Column(db.String(20), default='user', nullable=False)

    def __init__(self, name, username, email, company, password, role, power="user"):
        self.name = name
        self.username = username
        self.email = email
        self.company = company
        self.password_hash = generate_password_hash(password)
        self.role = role
        self.power = power

    @staticmethod
    def from_dict(data):
        user = User(
            name=data['name'],
            username=data['username'],
            email=data['email'],
            password=data['password'],
            power=data.get('power', 'user'),  # Default power is 'user' if not provided
            company=data['company'],
            role=data['role']
        )
        if 'id' in data:
            user.id = data['id']
        return user

    def to_dict(self):
        user_dict = {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password_hash': self.password_hash,
            'role': self.role,
            'company': self.company,
            'power': self.power
        }
        return user_dict

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
