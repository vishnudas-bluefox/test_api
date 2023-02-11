#!/usr/bin/env python3

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:8000",
]



class user_model(BaseModel):
    id: int
    name: str
    email: str
    gender: str
    status: str



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/public/v1/user")
async def user_registration(user_model:user_model):
    data = {
        "status":200,
        "message":"user successfully registered",
        "datas":user_model
    }
    print(data)
    return data
