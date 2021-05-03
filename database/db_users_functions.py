# async def db_check_jwt_user(user):
#     query = """ select * from users where username = :username """
#     values = { "username": user.username }

#     result = await fetch(query, False, values)
#     if result is None:
#         return None
#     else:
#         return result

# async def db_check_token_username(username):
#     query = """ select * from users where username = :username """
#     values = { "username": username }

#     result = await fetch(query, True, values)
#     if result is None:
#         return False
#     else:
#         return True

from database.config import users_collection

def jwtuser_helper(jwtuser) -> dict:
    return {
        "id": str(jwtuser["_id"]),
        "name": jwtuser["name"],
        "email": jwtuser["email"],
        "password": jwtuser['password'],
        "role": jwtuser['role']
    }


async def db_check_jwt_user(user): 
    users = users_collection.find({"username": user.username})
    if users: 
        
        result = []
        async for user in users:
            result.append(user)

        return result
    else:
        return None