from aiogram import Router
from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import types
from aiogram.types import KeyboardButton

router = Router()


@router.message(Command('temp'))
async def temp_check(message: Message):
    await message.answer("temp start")

    kb = [
        [KeyboardButton(text="check")]

    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="check"

    )
    await message.answer("Проверка температуры", reply_markup=keyboard)


