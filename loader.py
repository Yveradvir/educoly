from aiogram import Bot, Dispatcher
from dotenv  import load_dotenv
from os      import path, getenv, getcwd

from aiogram.contrib.fsm_storage.memory import MemoryStorage

load_dotenv(path.join(getcwd(), '.env'))

bot     = Bot(getenv("token"), parse_mode='html')
storage = MemoryStorage()
dp      = Dispatcher(bot, storage=storage)
