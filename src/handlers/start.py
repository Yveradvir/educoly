from loader  import dp
from aiogram import types

@dp.message_handler(commands=["/start"])
async def start(message: types.Message):
    await message.anwser("Welcome to the Educoly bot! Here you can adjust your scientific and educational process, schedule and more.")