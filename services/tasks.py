from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.task import Task


def get_user_tasks(
    db: Session,
    user_id: int
):

    return db.query(Task).filter(
        Task.user_id == user_id
    ).all()


def get_user_task(
    db: Session,
    user_id: int,
    task_id: int
):

    task = db.query(Task).filter(
        Task.id == task_id,
        Task.user_id == user_id
    ).first()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found for this user"
        )

    return task


def create_user_task(
    db: Session,
    user_id: int,
    task_data
):

    task = Task(
        name=task_data.name,
        user_id=user_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def update_user_task(
    db: Session,
    user_id: int,
    task_id: int,
    task_data
):

    task = get_user_task(
        db,
        user_id,
        task_id
    )

    task.name = task_data.name

    db.commit()
    db.refresh(task)

    return task


def patch_user_task(
    db: Session,
    user_id: int,
    task_id: int,
    task_data
):

    task = get_user_task(
        db,
        user_id,
        task_id
    )

    updates = task_data.model_dump(
        exclude_unset=True
    )

    for field, value in updates.items():

        if field == "name":
            task.name = value

    db.commit()
    db.refresh(task)

    return task


def delete_user_task(
    db: Session,
    user_id: int,
    task_id: int
):

    task = get_user_task(
        db,
        user_id,
        task_id
    )

    db.delete(task)
    db.commit()