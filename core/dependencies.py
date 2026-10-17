from sqlmodel import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Annotated

from database.database import SessionDep
from core.security import verify_token
from repositories.teacher_repo import get_data_by_email
from model.teacher import Teacher

oauth2 = OAuth2PasswordBearer(tokenUrl="/Teacher/login")

def get_current_teacher(token: Annotated[str, Depends(oauth2)], session : SessionDep)-> Teacher:

    email = verify_token(token)

    teacher = get_data_by_email(email,session)

    return teacher



