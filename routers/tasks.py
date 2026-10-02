from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies.common_parameters import current_user

from schemas.tasks import (
    TaskCreate,
    TaskUpdate,
    PatchTask,
    TaskResponse
)

from services.tasks import (
    get_user_tasks,
    get_user_task,
    create_user_task,
    update_user_task,
    patch_user_task,
    delete_user_task
)


router = APIRouter(
    prefix="/users/{user_id}/tasks",
    tags=["Tasks"]
)


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_tasks(
    user_id: int,
    db: Session = Depends(get_db),
    user=Depends(current_user)
):

    return get_user_tasks(
        db,
        user_id
    )


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    user_id: int,
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(current_user)
):

    return get_user_task(
        db,
        user_id,
        task_id
    )


@router.post(
    "/",
    response_model=TaskResponse
)
def create_task(
    user_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
    user=Depends(current_user)
):

    return create_user_task(
        db,
        user_id,
        task
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
def update_task(
    user_id: int,
    task_id: int,
    task: TaskUpdate,
    db: Session = Depends(get_db),
    user=Depends(current_user)
):

    return update_user_task(
        db,
        user_id,
        task_id,
        task
    )


@router.patch(
    "/{task_id}",
    response_model=TaskResponse
)
def patch_task(
    user_id: int,
    task_id: int,
    task: PatchTask,
    db: Session = Depends(get_db),
    user=Depends(current_user)
):

    return patch_user_task(
        db,
        user_id,
        task_id,
        task
    )


@router.delete(
    "/{task_id}"
)
def delete_task(
    user_id: int,
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(current_user)
):

    delete_user_task(
        db,
        user_id,
        task_id
    )

    return {
        "message": "Task deleted successfully"
    }