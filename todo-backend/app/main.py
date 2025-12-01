from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import auth_router, todo_router, user_router

app = FastAPI(title="Todo Backend")

origins = [
    "https://todo-mk3wmlm4m-pushpak-pandharpattes-projects.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router.router)
app.include_router(todo_router.router)
app.include_router(user_router.router)
