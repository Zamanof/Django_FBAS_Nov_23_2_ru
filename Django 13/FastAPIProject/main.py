
from fastapi import FastAPI, Query, Form
from fastapi.responses import (FileResponse,
                               HTMLResponse,
                               JSONResponse,
                               Response,
                               RedirectResponse)
from fastapi.encoders import jsonable_encoder

import html

app = FastAPI()


@app.get("/")
async def root():
    # return {"message": "Hello World"}
    return FileResponse("public/index.html")

@app.get("/file", response_class=FileResponse)
async def root_html():
    return "public/index.html"


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/get-image")
async def get_image():
    return FileResponse("public/deer.jpg", media_type="image/jpeg")

@app.get("/download-image")
async def download_image():
    return FileResponse("public/deer.jpg",
                        media_type="application/octet-stream",
                        filename="maral.jpg")

@app.get("/my-hello")
async def my_hello():
    html_code = "<h1 style='color:purple'>Nicheqo ne lezet na UM</h1>"
    return HTMLResponse(html_code)

@app.get("/get-json")
async def get_json():
    data = {'name':'Nadir', 'age': 45}
    json_data = jsonable_encoder(data)
    return JSONResponse(json_data)


@app.get("/get-text")
async def get_text():
    html_code = "<h1 style='color:purple'>Nicheqo ne lezet na UM</h1>"
    return Response(content=html_code, media_type="text/plain")



@app.get("/names/Nadir")
async def get_nadir():
    return {"name": "Hello, Nadir"}


@app.get("/names/{name}")
async def get_names(name):
    return {"name": name}


# @app.get("/cars")
# async def get_car(car = Query()):
#     return {"car": car}


@app.get("/cars")
async def get_cars(car: list[str]=Query()):
    return {"cars": car}


@app.get("/foo")
async def get_foo():
    return RedirectResponse('/')


@app.post("/login", response_class=HTMLResponse)
async def login(email: str=Form(...), password: str=Form(...)):
    page = f"<h1 style='color:turquoise'>Hello {html.escape(email)}!!! Password: {html.escape(password)}. Please dont hack me!!</h1>"
    return page


