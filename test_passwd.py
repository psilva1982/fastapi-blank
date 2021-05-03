from utils.security import get_hashed_password, verify_password

def test_password_hash():
    print(get_hashed_password('test'))

test_password_hash()

test2 = verify_password('test', get_hashed_password('test'))
print(test2)