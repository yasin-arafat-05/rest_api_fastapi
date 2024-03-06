from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta,datetime
from passwrdHassing import verify_password
from database import SessionLocal
from dotenv import dotenv_values
from jose import jwt
import models

ASSESS_TOKEN_EXPIRE_MINUTES = 180
asses_credential  = dotenv_values(".env")

router = APIRouter(
    ["login"]
)


@router.post('/token')
async def access_token_for_login(req : OAuth2PasswordRequestForm =Depends()):
    user = authenticate_user(req.email,req.passwrd)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect Credientials",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    assess_token_expire = timedelta(minutes=ASSESS_TOKEN_EXPIRE_MINUTES)
    assess_token = create_access_token(data={"id":user["id"],
                                       "email":user["email"],},
                                       expires_delta= assess_token_expire
                                       )
    return assess_token

    
def authenticate_user(email:str, passwrd:str ):
    db = SessionLocal()
    user = db.query(models.User).filter(models.User.email==email).first()
    if not user:
        return False
    if not verify_password(passwrd,user["password"]):
        return False 
   
    return True
    
def create_access_token(data:dict,expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=6)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,asses_credential["SECRECT_KEY"],algorithm=asses_credential["ALGORITHM"])
    return encode_jwt
    
    