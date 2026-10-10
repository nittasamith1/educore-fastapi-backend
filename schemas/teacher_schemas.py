from pydantic import BaseModel, EmailStr

class TeacherBase(BaseModel):
    id : int
    name : str
    email : EmailStr
    department : str

class TeacherCreate(BaseModel):
    name : str
    email : EmailStr
    department : str
    password : str

class TeacherUpdate(BaseModel):
    name : str
    email : EmailStr
    password : str
    department : str
