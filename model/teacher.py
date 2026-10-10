from sqlmodel import SQLModel, Field
from pydantic import EmailStr


class Teacher(SQLModel, table = True):
    id : int | None  = Field(default = None , primary_key = True)
    name : str 
    email : EmailStr = Field(unique = True, index = True)
    password : str 
    department : str


