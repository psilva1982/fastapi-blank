# async def db_check_jwt_user(user):
#     query = """ select * from users where username = :username """
#     values = { "username": user.username }

#     result = await fetch(query, False, values)
#     if result is None:
#         return None
#     else:
#         return result

from database.config import users_collection

async def db_check_jwt_user(user): 
    user = await users_collection.find_one({"username": user.username})
    if user:
        print(user)
        return user 
    else:
        return None

# async def db_check_token_username(username):
#     query = """ select * from users where username = :username """
#     values = { "username": username }

#     result = await fetch(query, True, values)
#     if result is None:
#         return False
#     else:
#         return True