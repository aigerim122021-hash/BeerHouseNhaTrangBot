import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from os import getenv

TOKEN = getenv("TELEGRAM_BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привет! Бот работает.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())