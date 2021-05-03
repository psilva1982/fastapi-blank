from typing import Optional
from pydantic import BaseModel
from fastapi import Query
from bson import ObjectId

class PersonSchema(BaseModel):
    _id: ObjectId
    name: Optional[str] 
    mail: Optional[str] = Query(None, regex='^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$')
    phone: Optional[str]