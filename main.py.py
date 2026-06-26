import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.types import BotCommand

TOKEN = "8798897292:AAGKc4g4Wh3KwDB9xInl5eLrRDYnBOseLp4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start", "commands"))
async def commands_command(message: types.Message):
    menu_text = (
        "🗺️ **Список доступних карт і команд:**\n\n"
        "🏜️ **Mirage:**\n"
        "• /mirage_a — Раскидка А плента\n"
        "• /mirage_b — Раскидка Б плента\n"
        "• /mirage_mid — Раскидка мидла\n\n"
        "🌋 **Inferno:**\n"
        "• /inferno_a — Раскидка А плента\n"
        "• /inferno_b — Раскидка Б плента\n"
        "• /inferno_mid — Раскидка мидла\n\n"
        "🏙️ **Overpass:**\n"
        "• /overpass_a — Раскидка А плента\n"
        "• /overpass_b — Раскидка Б плента\n"
        "• /overpass_mid — Раскидка мидла\n\n"
        "ancient **Ancient:**\n"
        "• /ancient_a — Раскидка А плента\n"
        "• /ancient_b — Раскидка Б плента\n"
        "• /ancient_mid — Раскидка мидла\n\n"
        "🏛️ **Anubis:**\n"
        "• /anubis_a — Раскидка А плента\n"
        "• /anubis_b — Раскидка Б плента\n"
        "• /anubis_mid — Раскидка мидла\n\n"
        "🏭 **Nuke:**\n"
        "• /nuke_a — Раскидка А плента\n"
        "• /nuke_b — Раскидка Б плента (Б-завод)\n"
        "• /nuke_mid — Раскидка улицы (Улица/Улица-Мид)\n\n"
        "🕌 **Dust 2:**\n"
        "• /dust2_a — Раскидка А плента\n"
        "• /dust2_b — Раскидка Б плента\n"
        "• /dust2_mid — Раскидка мидла\n\n"
        "🟢 **Cache:**\n"
        "• /cache_a — Раскидка А плента\n"
        "• /cache_b — Раскидка Б плента\n"
        "• /cache_mid — Раскидка мидла\n\n"
        "💡 *Просто натисни на синю команду, щоб побачити розкидку!*"
    )
    await message.answer(menu_text, parse_mode="Markdown")


# ================= ХЕНДЛЕРИ: MIRAGE =================

@dp.message(Command("mirage_a"))
async def mirage_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Mirage A, чтобы узнать его ID")

@dp.message(Command("mirage_b"))
async def mirage_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Mirage B, чтобы узнать его ID")

@dp.message(Command("mirage_mid"))
async def mirage_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда video для Mirage Mid, чтобы узнать его ID")


# ================= ХЕНДЛЕРИ: INFERNO =================

@dp.message(Command("inferno_a"))
async def inferno_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Inferno A")

@dp.message(Command("inferno_b"))
async def inferno_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Inferno B")

@dp.message(Command("inferno_mid"))
async def inferno_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Inferno Mid")


# ================= ХЕНДЛЕРИ: OVERPASS =================

@dp.message(Command("overpass_a"))
async def overpass_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Overpass A")

@dp.message(Command("overpass_b"))
async def overpass_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Overpass B")

@dp.message(Command("overpass_mid"))
async def overpass_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Overpass Mid")


# ================= ХЕНДЛЕРИ: ANCIENT =================

@dp.message(Command("ancient_a"))
async def ancient_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Ancient A")

@dp.message(Command("ancient_b"))
async def ancient_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Ancient B")

@dp.message(Command("ancient_mid"))
async def ancient_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Ancient Mid")


# ================= ХЕНДЛЕРИ: ANUBIS =================

@dp.message(Command("anubis_a"))
async def anubis_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Anubis A")

@dp.message(Command("anubis_b"))
async def anubis_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Anubis B")

@dp.message(Command("anubis_mid"))
async def anubis_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Anubis Mid")


# ================= ХЕНДЛЕРИ: NUKE =================

@dp.message(Command("nuke_a"))
async def nuke_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Nuke A")

@dp.message(Command("nuke_b"))
async def nuke_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Nuke B")

@dp.message(Command("nuke_mid"))
async def nuke_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Nuke Mid")


# ================= ХЕНДЛЕРИ: DUST 2 =================

@dp.message(Command("dust2_a"))
async def dust2_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Dust 2 A")

@dp.message(Command("dust2_b"))
async def dust2_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Dust 2 B")

@dp.message(Command("dust2_mid"))
async def dust2_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Dust 2 Mid")


# ================= ХЕНДЛЕРИ: CACHE =================

@dp.message(Command("cache_a"))
async def cache_a_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Cache A")

@dp.message(Command("cache_b"))
async def cache_b_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Cache B")

@dp.message(Command("cache_mid"))
async def cache_mid_cmd(message: types.Message):
    await message.answer("Отправь сюда видео для Cache Mid")

# Хендлер, який ловить надіслані відео та повертає їх ID
@dp.message(F.video)
async def get_video_id(message: types.Message):
    await message.answer(f"Твій ID відео:\n` {message.video.file_id} `", parse_mode="Markdown")
    

import asyncio
import os
from aiohttp import web

async def main():
    print("Бот успешно запущен!")
    
    # 1. Запускаем пустышку-сервер для Render
    app = web.Application()
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    # 2. Добавляем команду /start в кнопку Меню
    commands = [
        BotCommand(command="start", description="Главное меню / Запустить бота")
    ]
    await bot.set_my_commands(commands)

    # 3. Жёстко сбрасываем все прошлые зависшие подключения
    await bot.session.close()
    await asyncio.sleep(1)
    await bot.delete_webhook(drop_pending_updates=True)

    # 4. Запускаем чистый поллинг
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
