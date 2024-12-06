# ختص بحماية المعلومات ومعرفة من هو المستخدم و المصادقة
#[@]  راجعه لاحقا
# هذه الصفحة خاة بتسجيل الدخول
# database migration ابحث عنه
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from .. import database, schemas, models, utils, oauth2 

router = APIRouter(tags=['Authentication'])

# @router.post('/login')1
@router.post('/login', response_model=schemas.Token)
# def login(user_credentials:schemas.UserLogen, db: Session = Depends(database.get_db)):1
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):

    
    # user = db.query(models.User).filter(models.User.email == user_credentials.email).first()1
    {
        "username": "asdf",
        "password": "aldghf"
    }
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentals")1
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentals")
    
    if not utils.verify(user_credentials.password, user.password):
        # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentals")1
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentals")


# create a token
    access_token = oauth2.create_access_token(data = {"user_id": user.id})


# return token


    # return {"token": "example token"}1
    return {"access_token" : access_token, "token_type": "bearer"}