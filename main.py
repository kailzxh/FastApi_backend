from fastapi import FastAPI

from routers.tasks import router as task_router
from routers.users import router as user_router


app = FastAPI()


app.include_router(user_router)
app.include_router(task_router)


@app.get("/")
def home():

    return {
        "message": "Task API is running"
    }