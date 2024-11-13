from aiogram import Bot, Dispatcher, types
from aiogram.enums.parse_mode import ParseMode
from utils.db.postgres import Database
from aiogram.client.bot import DefaultBotProperties
from data.config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML))
db = Database()
