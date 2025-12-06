import aiogram
import sqlite
import logging
import asyncio

from aiogram import Bot, Dispatcher

TOKEN = 'TOKEN"

bot = Bot(Token=TOKEN)
dp = Dispatcher()
router = Router(name=Name)


@router.message(Command('start'))
async def start_command(Command('start')
  await message.reply('hello world')
