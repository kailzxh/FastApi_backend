from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TaskCreate(BaseModel):
    name: str


class TaskUpdate(BaseModel):
    name: str


class PatchTask(BaseModel):
    name: str | None = None


class TaskResponse(BaseModel):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True