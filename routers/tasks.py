from fastapi import APIRouter, Depends

from dependencies.common_parameters import current_user

from schemas.tasks import (
    TaskCreate,
    TaskUpdate,
    PatchTask
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
    prefix="/users/tasks",
    tags=["Tasks"]
)


@router.get("/")
def get_tasks(
    
    user=Depends(current_user)
):

    return {
        "user": user,
        "tasks": get_user_tasks(user["id"])
    }


@router.get("/{task_id}")
def get_task(
    task_id: int,
    user=Depends(current_user)
):

    return get_user_task(user["id"], task_id)


@router.post("/")
def create_task(
    task: TaskCreate,
    user=Depends(current_user)
):

    return create_user_task(user["id"], task)


@router.put("/{task_id}")
def update_task(
    user_id: int,
    task_id: int,
    task: TaskUpdate,
    user=Depends(current_user)
):

    return update_user_task(
        user_id,
        task_id,
        task
    )


@router.patch("/{task_id}")
def patch_task(
    user_id: int,
    task_id: int,
    task: PatchTask,
    user=Depends(current_user)
):

    return patch_user_task(
        user_id,
        task_id,
        task
    )


@router.delete("/{task_id}")
def delete_task(
    user_id: int,
    task_id: int,
    user=Depends(current_user)
):

    delete_user_task(
        user_id,
        task_id
    )

    return {
        "message": "Task deleted successfully"
    }