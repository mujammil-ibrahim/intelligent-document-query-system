from dotenv import load_dotenv
from pathlib import Path
import os

# Absolute path to the project .env
env_path = Path(__file__).resolve().parent.parent / ".env"

print("Loading .env from:", env_path)

# Load .env FIRST
load_dotenv(dotenv_path=env_path)

# Now read environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")

print("DATABASE_URL =", DATABASE_URL)
print("MODEL_NAME =", MODEL_NAME)
print("OPENROUTER_API_KEY Loaded:", OPENROUTER_API_KEY is not None)