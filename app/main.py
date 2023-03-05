from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

# print(settings.database_username)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware, #middleware is a function that runs before any request
    allow_origins=origins, #domain that can talk to our API
    allow_credentials=True, 
    allow_methods=["*"], #http method that can talk to our API, i.e. only get request
    allow_headers=["*"], 
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
        
@app.get("/")
def root():
    return {"message": "Hello World"}
