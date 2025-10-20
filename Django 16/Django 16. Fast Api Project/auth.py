from datetime import datetime, timedelta

from passlib.context import CryptContext

from jose import jwt, JWTError

from typing import Optional

SECRET_KEY = "ef033df0791d-4275-b2ad-7ff3a6cfa789"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt_sha256", "bcrypt"], deprecated="auto")

def hash_password(raw: str)-> str:
    return pwd_context.hash(raw)


def verify_password(raw: str, hashed: str) -> bool:
    return pwd_context.verify(raw, hashed)


def create_access_token(sub:str,
                        role:str,
                        expires_minutes:int=ACCESS_TOKEN_EXPIRE_MINUTES
                        ) -> str:
    now = datetime.utcnow()
    payload = {
        'sub': sub,
        'role': role,
        'iat': now,
        'exp': now + timedelta(minutes=expires_minutes)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token:str) -> Optional[dict]:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
