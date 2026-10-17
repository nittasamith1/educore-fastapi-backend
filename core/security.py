from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException,status
from jwt.exceptions import InvalidTokenError

from core.config import sec_settings

password_context = CryptContext(
schemes=["bcrypt"],
deprecated="auto"
)

def hash_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(plain_password : str, hash_password : str):
    return password_context.verify(plain_password, hash_password)


def create_token(email:str) -> str:
    payload = {
        'sub' : email,
        'exp' : datetime.now() + timedelta(days = 1)
    }

    token = jwt.encode(
        payload=payload,
        algorithm= sec_settings.JWT_ALGORITHM,
        key = sec_settings.JWT_SECRET_KEY
    )

    return token

def verify_token(token : str):
    try:
        payload = jwt.decode(
            jwt = token,
            key = sec_settings.JWT_SECRET_KEY,
            algorithms=[sec_settings.JWT_ALGORITHM]
        )

        email = payload.get("sub")

        if not email:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                details = "Invalid Token",
                headers={"WWW.Authentication : Bearer"}
            )
        return email
    
    except InvalidTokenError:
        raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        details = "Invalid Token or Expired",
                        headers={"WWW.Authentication : Bearer"}
                    ) 



