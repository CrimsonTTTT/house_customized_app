from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.db.user import User


class UserDao:
    def __init__(self, db):
        self.db = db


    def create_user(self, name: str, password: str):
        user = User(username=name, password=password)
        self.db.session.add(user)
        self.db.session.commit()
        self.db.refresh(user)
        return user


