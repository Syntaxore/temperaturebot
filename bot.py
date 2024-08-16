import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from keyboards.keyboard import router as keyboard_router
from handlers.handler import router as handler_router

logging.basicConfig(level=logging.INFO)

bot = Bot(token='7430076650:AAG9aa4MMu-72fGrE2aE39VXt-ep7kkfDEk')

dp = Dispatcher()
dp.include_router(keyboard_router)
dp.include_router(handler_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())

    except KeyboardInterrupt:
            print("Bot OFF")