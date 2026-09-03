from fastapi import FastAPI, Depends, Response, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Annotated
from model.users import User
import uvicorn

import psycopg2
main_url = '127.0.0.1'
port = 8000

app = FastAPI()

from auth.fast_api_auth import auth_router
from web.user import auth_router
from web.books import books_router
from web.authors import authors_router

app.include_router(auth_router)
app.include_router(books_router)
app.include_router(authors_router)

if __name__ == '__main__':
    uvicorn.run(
        app,
        host = '127.0.0.1',
        port = 8000
    )