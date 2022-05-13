import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage



storage = MemoryStorage()
bot = Bot(token=os.environ['TG_API'])
dp = Dispatcher(bot, storage=storage)
