import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

TOKEN = os.getenv("BOT_TOKEN")  # Токен берётся из переменной окружения
CHANNEL_CHAT_ID = os.getenv("CHANNEL_CHAT_ID")  # Имя канала из переменной окружения

default_properties = DefaultBotProperties(parse_mode=ParseMode.HTML)
bot = Bot(token=TOKEN, default=default_properties)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Карта 1", callback_data="button_1")],
        [InlineKeyboardButton(text="Карта 2", callback_data="button_2")],
        [InlineKeyboardButton(text="Карта 3", callback_data="button_3")],
        [InlineKeyboardButton(text="Карта 4", callback_data="button_4")],
        [InlineKeyboardButton(text="Карта 5", callback_data="button_5")],
    ])
    await bot.send_message(
        chat_id=CHANNEL_CHAT_ID,
        text="что ОН думает о тебе?",
        reply_markup=keyboard
    )

@dp.callback_query(F.data == "button_1")
async def button_1_callback(callback: CallbackQuery):
    await callback.answer("он видит, что у тебя проблемы. но пока не знает как помочь.", show_alert=True)

@dp.callback_query(F.data == "button_2")
async def button_2_callback(callback: CallbackQuery):
    await callback.answer("он видит тебя секусальной и привлекательной. сейчас большой наплыв сексуального интереса.", show_alert=True)

@dp.callback_query(F.data == "button_3")
async def button_3_callback(callback: CallbackQuery):
    await callback.answer("он думает, что ты слишком беззаботная. его это смущает.", show_alert=True)

@dp.callback_query(F.data == "button_4")
async def button_4_callback(callback: CallbackQuery):
    await callback.answer("он знает про твою обиду. но пока не действует.", show_alert=True)

@dp.callback_query(F.data == "button_5")
async def button_5_callback(callback: CallbackQuery):
    await callback.answer("он следит за твоими соц сетями. ты ему очень интересна.", show_alert=True)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
