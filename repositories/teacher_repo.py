from sqlmodel import select
from fastapi import HTTPException

from schemas.teacher_schemas import TeacherCreate,TeacherBase, TeacherUpdate
from database.database import SessionDep
from model.teacher import Teacher
from core.security import hash_password


def get_all_data(session : SessionDep) -> list[TeacherBase]:
    teachers = session.exec(select(Teacher)).all()

    return teachers

def get_teacher_by_id(id : int , session : SessionDep) -> TeacherBase:

    teacher = session.get(Teacher, id )

    if teacher is None:
            raise HTTPException(
                        status_code=404,
                        detail="No Teachers Data is Available with this ID"
                    )

    return teacher

def insert_data(data : TeacherCreate, session : SessionDep) -> TeacherBase:

    session.add(data)
    session.commit()
    session.refresh(data)

    return data

def update_data(id : int, data : TeacherUpdate, session : SessionDep) -> TeacherBase:

    teacher = session.get(Teacher, id)

    if teacher is None:
            raise HTTPException(
                 status_code=404,
                 detail="Teacher with this ID is not Existed"
            ) 

    update_teacher = data.model_dump(exclude_unset=True)

    if "password" in update_teacher:
            update_teacher["password"] = hash_password(
                update_teacher["password"]
            )

    for k,v in update_teacher.items():
        setattr(teacher,k,v)

    session.add(teacher)
    session.commit()
    session.refresh(teacher)

    return teacher

def delete_teacher(id : int, session : SessionDep):
    teacher = session.get(Teacher, id)

    if teacher is None:
        raise HTTPException(
             status_code=404,
             detail="Teacher with this ID is not Existed"
        ) 

    session.delete(teacher)
    session.commit()

    return {
            "message": "Teacher Details Deleted Successfully",
            "id": id
        }







