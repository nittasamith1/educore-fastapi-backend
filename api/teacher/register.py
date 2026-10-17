from fastapi import APIRouter,Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm


from schemas.teacher_schemas import TeacherUpdate,TeacherCreate,TeacherBase
from database.database import SessionDep
from core.dependencies import get_current_teacher
from model.teacher import Teacher
from service.teacher_service import (
    teacher_data,
    teacher_register,
    teachers_data,
    modify_teacher,
    remove_teacher,
    login_token
)

router = APIRouter(prefix="/Teacher",tags=['Teachers'])

@router.post("/", response_model=TeacherBase)
def teacher_registration(
    data: TeacherCreate,
    session: SessionDep
):
    return teacher_register(data, session)

@router.post("/login")
def teacher_login(request_token : Annotated[OAuth2PasswordRequestForm, Depends()], session : SessionDep):
    return login_token(request_token.username,request_token.password,session)

@router.get("/me")
def get_my_profile(current_teacher : Annotated[Teacher, Depends(get_current_teacher)]):
    return {
        'id' : current_teacher.id,
        'email' : current_teacher.email,
        'name' : current_teacher.name,
        'department' : current_teacher.department
    }


@router.get("/", response_model=list[TeacherBase])
def get_teachers(
session: SessionDep
):
    return teachers_data(session)

@router.get("/{id}", response_model=TeacherBase)
def get_teacher(
id: int,
session: SessionDep
):
    return teacher_data(id, session)

@router.put("/{id}", response_model=TeacherBase)
def update_teacher(
id: int,
data: TeacherUpdate,
session: SessionDep
):
    return modify_teacher(id, data, session)

@router.delete("/{id}")
def delete_teacher_route(
id: int,
session: SessionDep
):
    return remove_teacher(id, session)




