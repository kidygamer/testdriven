from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # NEW
from tortoise import Tortoise  # NEW
from src.database.register import register_tortoise  # NEW
from src.database.config import TORTOISE_ORM         # NEW

from src.routes import users, notes

Tortoise.init_models(["src.database.models"], "models")  # NEW

app = FastAPI()

# NEW
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://10.10.132.214:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(notes.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

@app.get("/")
def home():
    return "Hello, World!"
