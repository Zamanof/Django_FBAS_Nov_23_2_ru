from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from jose import jwt
from sqlalchemy.orm import Session
from starlette import status
from auth import hash_password, verify_password, create_access_token
from models import User, Role
from deps import get_db, get_current_user
from schemas import UserOut, UserRegister, TokenOut, UserLogin

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


@router.post("/login", response_model=TokenOut, status_code=status.HTTP_200_OK)
def login(payload: UserLogin, db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if not user or not verify_password(payload.password, user.password_hash) or not user.is_active:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    token = create_access_token(sub=user.email, role=user.role.value)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me", response_model=UserOut, status_code=status.HTTP_200_OK)
def me(current:User = Depends(get_current_user)):
    return current