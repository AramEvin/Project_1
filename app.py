from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

# HTML шаблоны и статика
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Хранилище задач (в памяти для простоты)
tasks = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/add", response_class=HTMLResponse)
def add_task(request: Request, title: str = Form(...)):
    tasks.append(title)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})
