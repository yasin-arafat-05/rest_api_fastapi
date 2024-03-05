from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def output():
    return "this is api"
