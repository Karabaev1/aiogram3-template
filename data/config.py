import os

from environs import Env
from dotenv import load_dotenv

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN") # Bot Token
ADMINS = list(map(int, os.getenv("ADMINS", "").split(","))) # adminlar ro'yxati


DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
