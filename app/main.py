import uvicorn

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Depends, status, Request, Form
from pathlib import Path

app = FastAPI()  # initialize fastapi instance
templates = Jinja2Templates(directory='templates')  # define the templates directory for Jinja2 to look at
validations = Jinja2Templates(directory='validations')
expectations = Jinja2Templates(directory='expectations')
app.mount("/static", StaticFiles(directory="static"), name="static")  # define the directory for the static files

BASE_PATH = Path(__file__).resolve().parent


# landing page. includes only the title, buttons and the plot
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    print(BASE_PATH)
    return templates.TemplateResponse('index.html', {
        'request': request})


@app.get('/index.html', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request})


@app.get("/expectations/{page_name}", response_class=HTMLResponse)
async def show_expectations_page(request: Request, page_name: str):
    return expectations.TemplateResponse(page_name,
                                         {"request": request})


@app.get("/validations/{link1}/{link2}/{link3}/{page_name}",
         response_class=HTMLResponse)
async def show_validations_page(request: Request, link1, link2, link3, page_name: str):
    page_name = link1 + "/" + link2 + "/" + link3 + "/" + page_name
    # data = openfile(str(BASE_PATH) + '/validations/' + page_name)
    return validations.TemplateResponse(page_name, {"request": request})

# @app.get("/page/{page_name}", response_class=HTMLResponse)
# async def show_page(request: Request, page_name: str):
#     data = openfile(page_name+".md")
#     return templates.TemplateResponse("page.html", {"request": request, "data": data})


if __name__ == "__main__":
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=False, root_path="/")
