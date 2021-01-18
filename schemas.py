from pydantic import BaseModel


class Student(BaseModel):
    id: int
    username: str
    hashed_password: str
    jwt_token: str

    class Config:
        orm_mode = True
