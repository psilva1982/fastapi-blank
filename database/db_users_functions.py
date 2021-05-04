from database.config import users_collection

def jwtuser_helper(jwtuser) -> dict:
    return {
        "id": str(jwtuser["_id"]),
        "name": jwtuser["name"],
        "email": jwtuser["email"],
        "password": jwtuser['password'],
        "role": jwtuser['role']
    }

async def db_check_jwt_user(jwt_user): 
    users = users_collection.find({"username": jwt_user.username})
    if users: 
        
        result = []
        async for user in users:
            result.append(user)

        return result
    else:
        return None


async def db_check_token_username(username):
    user = users_collection.find_one({"username": username})
    if user is None:
        return False
    else:
        return True