import os
from dotenv import load_dotenv

# Charger les variables depuis le fichier .env
load_dotenv()

class Config:
    TOKEN_KEY = os.getenv("TOKEN_KEY", "token_read_huggingface")