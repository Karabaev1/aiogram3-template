import asyncpg
from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMINS

router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    try:
        user = await db.add_user(telegram_id=message.from_user.id,
                                 full_name=message.from_user.full_name,
                                 username=message.from_user.username)
    except asyncpg.exceptions.UniqueViolationError:
        user = await db.select_user(telegram_id=message.from_user.id)

    # Adminlarga xabar yuborish
    msg = f"Yangi foydalanuvchi qo'shildi: {message.from_user.full_name} \\(@{message.from_user.username}\\)"
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=admin, text=msg, parse_mode=ParseMode.MARKDOWN_V2)
        except Exception as error:
            logger.info(f"Admin {admin} ga xabar yuborilmadi. Xato: {error}")

    # Экранирование специального символа '!'
    welcome_message = f"Assalomu alaykum, {message.from_user.full_name}\\!"
    await message.answer(welcome_message, parse_mode=ParseMode.MARKDOWN_V2)
