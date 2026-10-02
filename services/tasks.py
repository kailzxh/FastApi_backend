from fastapi import HTTPException


tasks = {
    1: {
        "id": 1,
        "name": "Learn FastAPI",
        "user_id": 1
    },
    2: {
        "id": 2,
        "name": "Learn Python",
        "user_id": 1
    },
    3: {
        "id": 3,
        "name": "Learn React",
        "user_id": 2
    }
}


def get_user_tasks(user_id: int):

    user_tasks = []

    for task in tasks.values():

        if task["user_id"] == user_id:
            user_tasks.append(task)

    return user_tasks


def get_user_task(user_id: int, task_id: int):

    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    if task["user_id"] != user_id:
        raise HTTPException(
            status_code=404,
            detail="Task not found for this user"
        )

    return task


def create_user_task(user_id: int, task_data):

    new_id = max(tasks.keys(), default=0) + 1

    new_task = {
        "id": new_id,
        "name": task_data.name,
        "user_id": user_id
    }

    tasks[new_id] = new_task

    return new_task


def update_user_task(user_id: int, task_id: int, task_data):

    task = get_user_task(user_id, task_id)

    task["name"] = task_data.name

    return task


def patch_user_task(user_id: int, task_id: int, task_data):

    task = get_user_task(user_id, task_id)

    updates = task_data.model_dump(exclude_unset=True)

    for field, value in updates.items():

        if field == "name":
            task["name"] = value

    return task


def delete_user_task(user_id: int, task_id: int):

    get_user_task(user_id, task_id)

    del tasks[task_id]