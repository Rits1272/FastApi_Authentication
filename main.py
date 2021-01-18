from typing import List

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

app = FastAPI()

# Creating the database tables
models.Base.metadata.create_all(bind=engine)

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


@app.post("/api/register/")
def register(username: str, password: str, db: Session = Depends(get_db)):
    student = models.Student(username=username)
    student.hash_password(password)
    student.create_access_token(data={"sub": username})
    print(student.jwt_token) 
    db.add(student)
    db.commit()
    db.refresh(student)
    return {"message": "Student registered successfully"} 


@app.post("/api/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.username == username).first()
    if student.verify_password(password):
        return {"message": "Login Successfull", "status": 200, "token": student.jwt_token}
    else:
        return {"message": "Invalid Credentials", "status": 503}

