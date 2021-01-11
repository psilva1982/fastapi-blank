from models.people import PersonSchema
from pydantic.types import List
from fastapi import FastAPI, Body, File, Header, Depends, HTTPException, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from starlette.responses import Response
from utils.response import ResponseModel, ErrorResponseModel
from database.db_people_functions import add_people, retrieve_person, retrieve_people, delete_person

v2_people = APIRouter()

@v2_people.post("/", response_description="Person V2 data added into the database")
async def add_person_data(person: PersonSchema = Body(...)):
    person = jsonable_encoder(person)
    new_person = await add_people(person)
    return ResponseModel(new_person, "Person added successfully.")

@v2_people.get("/", response_description="People V2 retrieved")
async def get_people():
    students = await retrieve_people()
    if students:
        return ResponseModel(students, "People data retrieved successfully")
    return ResponseModel(students, "Empty list returned")