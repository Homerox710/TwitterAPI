# FastAPI
from fastapi import (
    FastAPI, # Class that contains the app
    uvicorn # Server where the app runs
    )

# Models
from models import(
    UserBase,
    UserLogin,
    User,
    Tweet
)

app = FastAPI()

app.get(path="/")
def home():
    return {"Twitter API":"Working!"}

if __name__ == "__main__":
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)