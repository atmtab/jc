import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

from db import *

API_TOKEN = '5697772650:AAF5xvSQM1EXPodru5V59FoJRU_V5VYIggw'

database = db('newDB.sqlite')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyborad1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

print(tolistview(database.get_branches()))
branches_kb = InlineKeyboardMarkup(inline_keyboard=True)
for i in (tolistview(database.get_branches())):
    temp = InlineKeyboardButton(text=i, callback_data='branch_' + str(i))
    branches_kb.insert(temp)
    print(branches_kb)

groups_kb = InlineKeyboardMarkup(inline_keyboard=True)
for i in (tolistview(database.get_groups_list(1))):
    temp = InlineKeyboardButton(text=i, callback_data='group' + str(i))
    groups_kb.insert(temp)


keyborad1.add("Домашнее задание", "Обратная связь")


@dp.message_handler(commands=['start', 'help'])
async def welcome(message: types.Message):
    await message.reply("Hello!", reply_markup=keyborad1)


@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == 'Домашнее задание':
        await message.reply("Выберите феллиал:", reply_markup=branches_kb)

        @dp.callback_query_handler()
        async def kb_answer(call: types.CallbackQuery):
            if call.data == "fellial_1":
                await call.message.answer("Выберите группу:", reply_markup=groups_kb)
    elif message.text == 'Обратная связь':
        await message.reply("Выберите феллиал:", reply_markup=branches_kb)
    else:
        await message.answer(f'Your message is {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
