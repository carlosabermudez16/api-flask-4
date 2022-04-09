import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = True
    host = os.getenv("HOST")
    database = os.getenv("DATABASE") 
    user = os.getenv("USER")
    password = os.getenv("PASSWORD")

debug_mode = { 'development': Config }