from pydantic import BaseModel
from fastapi import Query
from models.security.role import Role

class User(BaseModel):
    name: str 
    password: str 
    mail: str = Query(..., regex='^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
    role: Role