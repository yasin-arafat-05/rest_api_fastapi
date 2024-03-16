from current_active_user import get_current_user
from passwrdHassing import verify_password
from fastapi import APIRouter,Depends
from database import SessionLocal
from sqlalchemy.orm import Session
from auth import schemas

router = APIRouter(tags=['Password Management'])

# db utilites
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()
       
@router.post('/forget/password')
async def forget_password():
    pass


@router.post('/reset/password')
async def reset_password(req : schemas.ResetPassword,
                         user : str = Depends(get_current_user),
                         db : Session = Depends(get_db)):
    try:
        if not verify_password(req.old_password, user.password):
            return {"details" : {"Wrong Password."}}
        if req.new_password != req.confirm_password:
            return {"details" : {"New And Confirm Password Don't Match."}}
        user.password = req.new_password
        db.commit()
        return {"details" : {"Password change Successfull."}}
    except Exception as e:
        print(f"Exception: {e}")