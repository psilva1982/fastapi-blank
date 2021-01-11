from routes.v1.people_router import v1_people
from routes.v2.people_router import v2_people 
from fastapi import APIRouter

app_v1 = APIRouter()

app_v1.include_router(v1_people, prefix="/people")

app_v2 = APIRouter() 
app_v2.include_router(v2_people, prefix="/people")