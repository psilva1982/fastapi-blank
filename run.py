from fastapi.exceptions import HTTPException
from fastapi import FastAPI, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from starlette.applications import Starlette
from routes.versions import app_v1, app_v2
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI(title="Blank Project", description='FastAPI Blank Project with MongoDB', version='0.0.1')

app.include_router(app_v1, prefix="/v1")
app.include_router(app_v2, prefix="/v2")