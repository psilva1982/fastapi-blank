import motor.motor_asyncio
from utils.constants import DB_URL

client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
database = client.blank

people_collection = database.get_collection("people")
users_collection = database.get_collection("users")