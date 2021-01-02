from sqlalchemy import Column, Integer, String
from database import Base
from passlib.apps import custom_app_context as pwd_context


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(122), unique=True, index=True)
    hashed_password = Column(String)

    def hash_password(self, password):
        self.hashed_password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)

