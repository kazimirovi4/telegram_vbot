from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from database import sqlite_db

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита!', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Vkusno_RogBot')

# @dp.message_handler(commands=['Режим_работы'])
async def vkusno_open(message : types.Message):
    await bot.send_message(message.from_user.id, 'Пн-Пт с 17:00 до 21:00\nСб-Вс с 18:00 до 23:00')

# @dp.message_handler(commands=['Расположение'])
async def vkusno_addreass(message : types.Message):
    await bot.send_message(message.from_user.id, 'Рогачев, ул.Михаила Фрунзе, 21А')
    await bot.send_location(message.from_user.id, longitude='30.044534', latitude='53.074026')

async def vkusno_menu_command(message : types.Message):
    await sqlite_db.sql_read(message)

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(vkusno_open, commands=['Режим_работы'])
    dp.register_message_handler(vkusno_addreass, commands=['Расположение'])
    dp.register_message_handler(vkusno_menu_command, commands=['Меню'])
