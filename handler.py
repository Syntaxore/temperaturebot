from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from temperture_windows import get_cpu_usage
from aiogram import types
from aiogram.types import KeyboardButton

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer("Hello!")


@router.message(F.text.lower() == 'check')
async def start_temp(message: types.Message):
    await message.reply(f"Загруженность процессора {get_cpu_usage()} %")