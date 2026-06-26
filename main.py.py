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
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Mirage (А плент)")

@dp.message(Command("mirage_b"))
async def mirage_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Mirage (Б плент)")

@dp.message(Command("mirage_mid"))
async def mirage_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Mirage (Мидл)")


# ================= ХЕНДЛЕРИ: INFERNO =================

@dp.message(Command("inferno_a"))
async def inferno_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Inferno (А плент)")

@dp.message(Command("inferno_b"))
async def inferno_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Inferno (Б плент)")

@dp.message(Command("inferno_mid"))
async def inferno_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Inferno (Мидл)")


# ================= ХЕНДЛЕРИ: OVERPASS =================

@dp.message(Command("overpass_a"))
async def overpass_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Overpass (А плент)")

@dp.message(Command("overpass_b"))
async def overpass_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Overpass (Б плент)")

@dp.message(Command("overpass_mid"))
async def overpass_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Overpass (Мидл)")


# ================= ХЕНДЛЕРИ: ANCIENT =================

@dp.message(Command("ancient_a"))
async def ancient_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Ancient (А плент)")

@dp.message(Command("ancient_b"))
async def ancient_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Ancient (Б плент)")

@dp.message(Command("ancient_mid"))
async def ancient_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Ancient (Мидл)")


# ================= ХЕНДЛЕРИ: ANUBIS =================

@dp.message(Command("anubis_a"))
async def anubis_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Anubis (А плент)")

@dp.message(Command("anubis_b"))
async def anubis_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Anubis (Б плент)")

@dp.message(Command("anubis_mid"))
async def anubis_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Anubis (Мидл)")


# ================= ХЕНДЛЕРИ: NUKE =================

@dp.message(Command("nuke_a"))
async def nuke_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Nuke (А плент)")

@dp.message(Command("nuke_b"))
async def nuke_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Nuke (Б плент)")

@dp.message(Command("nuke_mid"))
async def nuke_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Nuke (Улица)")


# ================= ХЕНДЛЕРИ: DUST 2 =================

@dp.message(Command("dust2_a"))
async def dust2_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Dust 2 (А плент)")

@dp.message(Command("dust2_b"))
async def dust2_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Dust 2 (Б плент)")

@dp.message(Command("dust2_mid"))
async def dust2_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Dust 2 (Мидл)")


# ================= ХЕНДЛЕРИ: CACHE =================

@dp.message(Command("cache_a"))
async def cache_a_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Cache (А плент)")

@dp.message(Command("cache_b"))
async def cache_b_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Cache (Б плент)")

@dp.message(Command("cache_mid"))
async def cache_mid_cmd(message: types.Message):
    await message.answer_video(video="ID_ВІДЕО", caption="Вот раскидка на Cache (Мидл)")


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
