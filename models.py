from sqlalchemy import Column, Integer, String
from database import Base
from passlib.apps import custom_app_context as pwd_context
from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(122), unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String(20), index=True)
    jwt_token = Column(String(1024))

    def hash_password(self, password):
        self.hashed_password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)

    def create_access_token(self, data):
        to_encode = data.copy()
        self.jwt_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        

