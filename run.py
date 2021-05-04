from fastapi.exceptions import HTTPException
from fastapi import FastAPI, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.status import HTTP_401_UNAUTHORIZED
from routes.versions import app_v1, app_v2
from datetime import datetime
from models.security.jwt_user import JWTUser
from utils.security import authenticate_user, create_jwt_token, check_jwt_token, create_jwt_token_with_refresh

app = FastAPI(title="Blank Project", description='FastAPI Blank Project with MongoDB', version='0.0.1')

app.include_router(app_v1, prefix="/v1", dependencies=[Depends(check_jwt_token),])
app.include_router(app_v2, prefix="/v2", dependencies=[Depends(check_jwt_token),])

@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):

    jwt_user_dict = {"username": form_data.username, "password": form_data.password }
    jwt_user = JWTUser(**jwt_user_dict)

    user = await authenticate_user(jwt_user)
    if user is None:
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED) 
    
    jwt_token = create_jwt_token(user)
    jwt_refresh = create_jwt_token(user, 'refresh')

    return {
        "access_token": jwt_token,
        'refresh_token': jwt_refresh
    }

@app.post("/token/refresh")
async def get_token_with_refresh(refresh: str):

    check = await check_jwt_token(refresh)
    
    if check:
        jwt_token = create_jwt_token_with_refresh(refresh)

        return {
            "access_token": jwt_token,
            "refresh_token": refresh
        }

@app.middleware("http")
async def middleware(request: Request, call_next):

    start_time = datetime.utcnow()

    #Modify request here 
    # if not any(word in str(request.url) for word in ['/token', '/docs', '/openapi']):
    #     try:
    #         jwt_token = request.headers['Authorization'].split('Bearer ')[1]
    #         is_valid = await check_jwt_token(jwt_token)
    #     except Exception as e:
    #         print(e)
    #         is_valid = False
    
    #     if not is_valid:
    #         return Response("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)

    response = await call_next(request)
    #Modify response here 
    executation_time = (datetime.now() - start_time).microseconds
    response.headers['x-execution-time'] = str(executation_time)

    return response