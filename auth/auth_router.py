from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from passwrdHassing import get_hash_password
from database import SessionLocal
import schemas,models

router = APIRouter(
    tags=[
        'auth'
    ]
)

# db utility:
def get_db():
   db = SessionLocal()
   try:
       yield db
   finally:
       db.close()


@router.post('/sing_up')
async def sing_up(req: schemas.User,db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==req.email).first()
    # if the email is already exists:
    if user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Email already exists.")
        
    # set the default value and encript the password:
    user_data = user.dict(exclude_unset = True)
    user_data["password"] = get_hash_password(user_data["password"])
    
    try:
        new_user = models.User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise HTTPException(
           status_code=status.HTTP_400_BAD_REQUEST,
           detail= str(e)    
        )
        