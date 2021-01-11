from database.config import people_collection
from bson import ObjectId

# helpers
def people_helper(people) -> dict:
    return {
        "id": str(people["_id"]),
        "name": people["name"],
        "mail": people["mail"],
        "phone": people["phone"]
    }

# Retrieve all students present in the database
async def retrieve_people():
    people = []
    async for person in people_collection.find():
        people.append(people_helper(person))
    return people


# Add a new student into to the database
async def add_people(people_data: dict) -> dict:
    people = await people_collection.insert_one(people_data)
    new_people = await people_collection.find_one({"_id": people.inserted_id})
    return people_helper(new_people)


# Retrieve a student with a matching ID
async def retrieve_person(id: str) -> dict:
    person = await people_collection.find_one({"_id": ObjectId(id)})
    if person:
        return people_helper(person)


# Update a student with a matching ID
async def update_person(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    person = await people_collection.find_one({"_id": ObjectId(id)})
    if person:
        updated_person = await people_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_person:
            return True
        return False


# Delete a student from the database
async def delete_person(id: str):
    person = await people_collection.find_one({"_id": ObjectId(id)})
    if person:
        await people_collection.delete_one({"_id": ObjectId(id)})
        return True