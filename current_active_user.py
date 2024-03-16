from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import SessionLocal
from jose import jwt,JWTError
from dotenv import dotenv_values
import models

config_crediential = dotenv_values(".env")

#oauth2 scheme:
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# db utilites
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


#get the current user: when a user authorized:
async def get_current_user(token: str = Depends(oauth2_scheme),db : Session = Depends(get_db)):
    print(f"get_current_user: {token}")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.Please log in.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token,config_crediential['SECRECT_KEY'], algorithms=['HS256'])
        print(payload)
        id: str = payload.get("id")
        if id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.User).filter(models.User.id==id).first()
    return user
