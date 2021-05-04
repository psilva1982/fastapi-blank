#openssl rand -hex 32
from decouple import config

JWT_SECRET_KEY = config('JWT_SECRET_KEY')
JWT_ALGORITH = "HS256"
JWT_TOKEN_EXPIRATION_TIME_MINUTES = 1
JWT_REFRESH_TOKEN_EXPIRATION_TIME_MINUTES = 15

DB_HOST=config('DB_HOST')
DB_DATABASE=config('DB_DATABASE')
DB_USER=config('DB_USER')
DB_PASS=config('DB_PASS')

DB_URL=f"mongodb+srv://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_DATABASE}?retryWrites=true&w=majority"