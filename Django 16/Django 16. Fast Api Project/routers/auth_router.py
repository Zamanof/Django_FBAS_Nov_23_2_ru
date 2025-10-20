from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status
from auth import hash_password
from models import User, Role
from deps import get_db
from schemas import UserOut, UserRegister

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register",
             response_model=UserOut,
             status_code=status.HTTP_201_CREATED)
def register(payload: UserRegister, db:Session=Depends(get_db)):
    exists = db.query(User).filter(User.email == payload.email).first()
    if exists:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        email=str(payload.email),
        password_hash=hash_password(payload.password),
        role=payload.role or Role.user
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
