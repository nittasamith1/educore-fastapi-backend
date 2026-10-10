from sqlmodel import Session

from database.database import engine
from model.teacher import Teacher
from repositories.teacher_repo import (
    get_all_data,
    get_teacher_by_id,
)


def test_get_all_teachers():
    with Session(engine) as session:
        teachers = get_all_data(session)

        assert isinstance(teachers, list)


def test_get_teacher_by_id():
    with Session(engine) as session:
        teachers = get_all_data(session)

        if teachers:
            teacher = get_teacher_by_id(
                teachers[0].id,
                session
            )

            assert teacher.id == teachers[0].id