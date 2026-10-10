from fastapi import APIRouter

from schemas.teacher_schemas import TeacherUpdate,TeacherCreate,TeacherBase
from database.database import SessionDep
from model.teacher import Teacher
from service.teacher_service import (
    teacher_data,
    teacher_register,
    teachers_data,
    modify_teacher,
    remove_teacher
)

router = APIRouter(prefix="/Teacher",tags=['Teachers'])

@router.post("/", response_model=TeacherBase)
def teacher_registration(
    data: TeacherCreate,
    session: SessionDep
):
    return teacher_register(data, session)

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




