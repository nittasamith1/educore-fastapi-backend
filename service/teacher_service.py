from sqlmodel import Session


from schemas.teacher_schemas import TeacherCreate,TeacherUpdate
from model.teacher import Teacher
from core.security import hash_password
from repositories.teacher_repo import (
    get_all_data,
    get_teacher_by_id,
    update_data,
    insert_data,
    delete_teacher
)


def teacher_register(data : TeacherCreate, session : Session):
    teacher = Teacher(
        **data.model_dump(exclude={'password'}),
        password= hash_password(data.password)
    )

    return insert_data(teacher,session)

def teachers_data(session:Session):
    return get_all_data(session)

def teacher_data(id:int, session:Session):

    return get_teacher_by_id(id,session)

def remove_teacher(id:int , session:Session):
    return delete_teacher(id,session)


def modify_teacher(id:int, data: TeacherUpdate, session : Session):
    return update_data(id,data,session)

