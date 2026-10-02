from pydantic import BaseModel


class TaskCreate(BaseModel):
    name: str


class TaskUpdate(BaseModel):
    name: str


class PatchTask(BaseModel):
    name: str | None = None


class Task(BaseModel):
    id: int
    name: str
    user_id: int


class User(BaseModel):
    id: int
    name: str