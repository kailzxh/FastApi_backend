from fastapi import HTTPException


users = {
    1: {
        "id": 1,
        "name": "Kailash"
    },
    2: {
        "id": 2,
        "name": "Rahul"
    }
}


def get_user(user_id: int):

    user = users.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def get_current_user():

    user = users.get(1)

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated"
        )

    return user