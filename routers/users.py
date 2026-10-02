from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies.common_parameters import current_user

from schemas.tasks import (
    UserCreate,
    UserResponse
)

from services.users import (
    create_user,
    get_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post(
    "/",
    response_model=UserResponse
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(
        db,
        user.name
    )


@router.get(
    "/me",
    response_model=UserResponse
)
def get_my_profile(
    user=Depends(current_user)
):

    return user


@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user_profile(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_user(
        db,
        user_id
    )