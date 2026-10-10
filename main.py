from fastapi import FastAPI
from contextlib import asynccontextmanager
from scalar_fastapi import get_scalar_api_reference

from database.database import create_db_tables
from api.teacher.register import router as teacher_router

@asynccontextmanager
async def lifespan(app : FastAPI):
    create_db_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(teacher_router)


@app.get("/scalar",include_in_schema= False)
def scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title = "API DOCUMENTATION"
    )



