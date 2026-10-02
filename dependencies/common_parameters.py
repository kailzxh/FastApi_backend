from fastapi import Depends
from sqlalchemy.orm import Session

from database import get_db
from services.users import get_current_user


def current_user(
    db: Session = Depends(get_db)
):

    return get_current_user(db)