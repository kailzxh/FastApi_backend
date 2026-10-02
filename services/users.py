from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.user import User


def create_user(db: Session, name: str):

    user = User(
        name=name
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def get_user(db: Session, user_id: int):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


def get_current_user(db: Session):

    # Temporary for learning.
    # Later JWT will determine the user.
    user = db.query(User).filter(
        User.id == 1
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not authenticated"
        )

    return user