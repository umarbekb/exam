import asyncio
import logging
import os
from datetime import datetime

from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command

from aiogram.types import BotCommand
from dotenv import load_dotenv

from db import User, Session, Message

load_dotenv('.env')
router = Router()
bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)


async def main() -> None:
    bot_instance = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    commands = [
        BotCommand(command="start", description="botni ishga tushurish uchun bosing")
    ]
    await bot_instance.set_my_commands(commands)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot_instance)


dp = Dispatcher()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    user = User(
        user_teg_id=str(message.from_user.id),
        username=message.from_user.username,
        created=datetime.utcnow()
    )
    session = Session()
    session.add(user)
    session.commit()
    await message.answer("Siz database ga qohildingiz")


@router.message()
async def save_msg(message: types.Message):
    user_id = str(message.from_user.id)
    text = message.text

    new_message = Message(user_id=user_id, text=text)

    session = Session()
    session.add(new_message)
    session.commit()
    session.close()

    await message.answer("Success")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
