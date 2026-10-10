from sqlmodel import SQLModel,Session,create_engine
from typing import Annotated
from fastapi import Depends

from core.config import settings


engine = create_engine(
    url = settings.DATABASE_URL,
    echo= True
)

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def get_db():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_db)]

