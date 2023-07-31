import os


DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

SQL_PATH = F"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

ACCESS_TOKEN_HUBSPOT = os.getenv("ACCESS_TOKEN_HUBSPOT")

URL_HUBSPOT="https://api.hubspot.com/crm/v3/objects/contacts"

OK = 200
INTERNAL_SERVER_ERROR = 500
