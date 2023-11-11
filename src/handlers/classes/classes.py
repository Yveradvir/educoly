import keyboards

from loader    import dp
from aiogram   import types 
from src.other import StatesForNewClasses

from aiogram.dispatcher.dispatcher import FSMContext


@dp.message_handler(commands=['nclass'])
async def nclass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['leader'] = message.from_user.id
        
    await StatesForNewClasses.waitForNameOfClass.set()
    await message.answer("Okay, what is the class, and how it works. The class is a room for your group where you can solute problems, homeworkes, look at the schedule. ")

@dp.message_handler(content_types=types.ContentTypes.TEXT, state=StatesForNewClasses.waitForNameOfClass)
async def waitForNameOfClass(message: types.Message, state: FSMContext):
    