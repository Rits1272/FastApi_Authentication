from typing import List

from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )


# Handling Session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("api/register")
def register(db: Session, user: schemas.Student):
    student = models.Student(username=user.username)
    student.hash_password(password)
    db.add(student)
    db.commit()
    db.refresh(student)
    return db_user


@app.post("api/login")
def login(db: Session, user: schemas.Student):
    username = user.username
    password = user.password

    student = db.query(models.Student).filter(models.User.username == username).first()
    if student.verify_password(password):
        return {"message": "Login Successfull", "status": 200}
    else:
        return {"message": "Invalid Credentials", "status": 503}

