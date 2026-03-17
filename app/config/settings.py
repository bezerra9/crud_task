import os 
from dotenv import load_dotenv

load_dotenv()

class Settings():
    DATABASE_URL: str = os.getenv('DATABASE_URL')
    DATABASE_NAME: str = "projeto_tasks"

settings = Settings()