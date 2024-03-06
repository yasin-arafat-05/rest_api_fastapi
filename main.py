from fastapi import FastAPI
from database import engine
import models

app = FastAPI()


# create all the metadata(table base on the models)
models.Base.metadata.create_all(bind=engine)

@app.get('/')
def output():
    return "this is api"

# sign up
from auth import sign_up
app.include_router(sign_up.router)
