# JWT تصفه
# [@]
# هذه الصفحة خاصة بكلمة المرور  
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

#SECRET_KEY
#Algorithm
#Expriaion time


# SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30 # المدى لجلب البينات يمكن الزيادة او النقصان
# ACCESS_TOKEN_EXPIRE_MINUTES = 1

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes # المدى لجلب البينات يمكن الزيادة او النقصان
# ACCESS_TOKEN_EXPIRE_MINUTES = 1

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentails_excption):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentails_excption
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentails_excption
    
    return token_data

# def get_current_user(token: str = Depends(oauth2_scheme)):1
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):

    credentails_exception  = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=
    "could not validate credentails", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentails_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
    # return verify_access_token(token, credentails_exception)1