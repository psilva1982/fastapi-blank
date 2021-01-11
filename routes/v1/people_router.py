from models.people import PersonSchema
from pydantic.types import List
from fastapi import FastAPI, Body, File, Header, Depends, HTTPException, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED
from starlette.responses import Response
from utils.response import ResponseModel, ErrorResponseModel
from database.db_people_functions import add_people, retrieve_person, retrieve_people, delete_person, update_person

v1_people = APIRouter()

@v1_people.post("/", response_description="Person data added into the database")
async def add_person_data(person: PersonSchema = Body(...)):
    person = jsonable_encoder(person)
    new_person = await add_people(person)
    return ResponseModel(new_person, "Person added successfully.")

@v1_people.get("/", response_description="People retrieved")
async def get_people():
    students = await retrieve_people()
    if students:
        return ResponseModel(students, "People data retrieved successfully")
    return ResponseModel(students, "Empty list returned")

@v1_people.get("/{id}", response_description="Person data retrieved")
async def get_person_data(id):
    person = await retrieve_person(id)
    if person:
        return ResponseModel(person, "Person data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Person doesn't exist.")

@v1_people.delete("/{id}", response_description="Person data deleted from the database")
async def delete_person_data(id: str):
    deleted_person = await delete_person(id)
    if deleted_person:
        return ResponseModel(
            "Person with ID: {} removed".format(id), "Person deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Person with id {0} doesn't exist".format(id)
    )

@v1_people.patch("/{id}")
async def update_person_data(id: str, req: PersonSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_person = await update_person(id, req)
    if updated_person:
        return ResponseModel(
            "Person with ID: {} name update is successful".format(id),
            "Person name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the Person data.",
    )