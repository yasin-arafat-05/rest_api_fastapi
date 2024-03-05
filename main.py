from fastapi import FastAPI

app  = FastAPI()

@app.get('/')
async def default():
    return "this is home route."
