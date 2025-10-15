from fastapi import FastAPI, Form, Depends
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class User(BaseModel):
    email: str
    password: str


@app.get("/")
async def root():
    return FileResponse("static/index.html")



@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def as_user_from_form(
        email: str = Form(...),
        password: str = Form(...)) -> User:
    return User(email=email, password=password)

@app.post("/login")
async def login(user: User = Depends(as_user_from_form)):
    return {"message": f"{user.email}"}


@app.post("/mylogin")
async def my_login(user: User):
    return {"message": f"{user.email}"}


