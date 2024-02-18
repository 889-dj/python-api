from fastapi import FastAPI

app = FastAPI()

#order of the routes does matter in fastapi

@app.get("/")
def root():
    return {"message":"welcome i m mj"}

@app.get("/posts")
def get_post():
    return {"data":"this is ur post"}