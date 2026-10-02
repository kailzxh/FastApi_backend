from fastapi import APIRouter, Depends

from dependencies.common_parameters import current_user
from services.users import get_user


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/me")
def get_my_profile(
    user=Depends(current_user)
):
    return user


@router.get("/")
def get_user_profile(user=Depends(current_user)):

    return get_user(user["id"])