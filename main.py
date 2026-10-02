from fastapi import FastAPI

from database import Base, engine

from models.user import User
from models.task import Task

from routers.users import router as user_router
from routers.tasks import router as task_router


Base.metadata.create_all(
    bind=engine
)


app = FastAPI()


app.include_router(user_router)
app.include_router(task_router)


@app.get("/")
def home():

    return {
        "message": "Task API is running"
    }
