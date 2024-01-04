# services/auth_service.py
from app.models.users import User, db

class AuthService:
    @staticmethod
    def register_user(name, username, email, company, password, role):
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            raise ValueError("Username already exists. Please choose a different username.")

        new_user = User(name=name, username=username, email=email, company=company, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if user:
            if user.check_password(password):
                return user
            else:
                return False
        return None

    def get_user_by_id(user_id):
        return User.query.get(user_id)

    def get_user_by_username(self, username):
        return User.query.filter_by(username=username).first()
