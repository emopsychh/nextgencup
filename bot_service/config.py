from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")

BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
CLIENT_ID = os.getenv("CHALLENGERMODE_CLIENT_ID")
REFRESH_KEY = os.getenv("CHALLENGERMODE_REFRESH_KEY")