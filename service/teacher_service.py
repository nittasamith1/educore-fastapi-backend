from sqlmodel import Session
from fastapi import HTTPException


from schemas.teacher_schemas import TeacherCreate,TeacherUpdate
from model.teacher import Teacher
from core.config import sec_settings
from core.security import hash_password,verify_password, create_token
from repositories.teacher_repo import (
    get_all_data,
    get_teacher_by_id,
    update_data,
    insert_data,
    delete_teacher,
    get_data_by_email
)


def teacher_register(data : TeacherCreate, session : Session):
    teacher = Teacher(
        **data.model_dump(exclude={'password'}),
        password= hash_password(data.password)
    )

    return insert_data(teacher,session)

def login_token(email : str, password:str, session : Session):
    teacher = get_data_by_email(email,session)

    if not verify_password(password, teacher.password):
        raise HTTPException(
            status_code=404,
            detail= "Entered Password is Wrong"
        )

    token = create_token(teacher.email)

    return {
        'token' : token,
        "token_type": "bearer"
    }

  
def teachers_data(session:Session):
    return get_all_data(session)

def teacher_data(id:int, session:Session):

    return get_teacher_by_id(id,session)

def remove_teacher(id:int , session:Session):
    return delete_teacher(id,session)


def modify_teacher(id:int, data: TeacherUpdate, session : Session):
    return update_data(id,data,session)

