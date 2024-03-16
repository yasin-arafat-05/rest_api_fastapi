from fastapi import FastAPI,Depends
from current_active_user import get_current_user
from database import engine
import models


app = FastAPI()


# create all the metadata(table base on the models)
models.Base.metadata.create_all(bind=engine)


# sign up and login 
from auth import sign_up,log_in
app.include_router(sign_up.router)
app.include_router(log_in.router)


# forget and reset password
from auth import passwrd
app.include_router(passwrd.router)
