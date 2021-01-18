from dotenv import load_dotenv
from os import environ

load_dotenv()

MONGO = environ.get('MONGO')
