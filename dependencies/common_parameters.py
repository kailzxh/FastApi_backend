from fastapi import Depends

from services.users import get_current_user


def current_user(user=Depends(get_current_user)):
    return user