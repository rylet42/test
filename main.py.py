import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

TOKEN = "8798897292:AAFjRVf3xFBmMLIEIviAs77P-7joJPmtILg"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- КЛАВИАТУРЫ (ИНЛАЙН-КНОПКИ) ---

# Главное меню: теперь со всеми картами в два столбца, чтобы красиво выглядело
maps_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Dust 2", callback_data="map_dust2"), InlineKeyboardButton(text="Mirage", callback_data="map_mirage")],
    [InlineKeyboardButton(text="Ancient", callback_data="map_ancient"), InlineKeyboardButton(text="Inferno", callback_data="map_inferno")],
    [InlineKeyboardButton(text="Cache", callback_data="map_cache"), InlineKeyboardButton(text="Anubis", callback_data="map_anubis")],
    [InlineKeyboardButton(text="Overpass", callback_data="map_overpass"), InlineKeyboardButton(text="Nuke", callback_data="map_nuke")]
])

def get_position_kb(map_name):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="A Плент", callback_data=f"pos_{map_name}_a")],
        [InlineKeyboardButton(text="B Плент", callback_data=f"pos_{map_name}_b")],
        [InlineKeyboardButton(text="Мид (Mid)", callback_data=f"pos_{map_name}_mid")],
        [InlineKeyboardButton(text="⬅️ Назад к картам", callback_data="back_to_maps")]
    ])

def get_grenade_kb(map_name, position):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💨 Смок", callback_data=f"gren_{map_name}_{position}_smoke"),
         InlineKeyboardButton(text="🔥 Молотов", callback_data=f"gren_{map_name}_{position}_molotov")],
        [InlineKeyboardButton(text="✨ Флешка", callback_data=f"gren_{map_name}_{position}_flash"),
         InlineKeyboardButton(text="💥 ХЕ (Хаешка)", callback_data=f"gren_{map_name}_{position}_he")],
        [InlineKeyboardButton(text="⬅️ Назад к позициям", callback_data=f"back_to_pos_{map_name}")]
    ])


# --- ХЕНДЛЕРЫ ---

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Выбери карту для раскидки:", reply_markup=maps_kb)

# Функция отлова видео для получения ID
@dp.message(F.video)
async def get_video_id(message: Message):
    await message.answer(f"ID твоего видео:\n`{message.video.file_id}`", parse_mode="MarkdownV2")

@dp.callback_query(F.data.startswith("map_"))
async def select_map(callback: CallbackQuery):
    map_name = callback.data.split("_")[1]
    await callback.message.edit_text(
        text=f"Карта: *{map_name.capitalize()}*\nВыбери часть карты:",
        reply_markup=get_position_kb(map_name),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("pos_"))
async def select_position(callback: CallbackQuery):
    data = callback.data.split("_")
    map_name = data[1]
    position = data[2]
    
    await callback.message.edit_text(
        text=f"Карта: *{map_name.capitalize()}* ➡️ Позиция: *{position.upper()}*\nКакая граната нужна?",
        reply_markup=get_grenade_kb(map_name, position),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data.startswith("gren_"))
async def send_grenade_info(callback: CallbackQuery):
    data = callback.data.split("_")
    map_name = data[1]       
    position = data[2]       
    grenade_type = data[3]   
    
    video_id = None

    # ==================== MIRAGE ====================
    if map_name == "mirage":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "BAACAgIAAxkBAAMfaj1hnVEi1YOGSQpmhrU8q69x7t4AAhmcAAK4quhJvfSP2Et1G608BA"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "BAACAgIAAxkBAAMhaj1htD6svKDisnzOWjHvv4HLlgIAAhqcAAK4quhJWq6JktWJXdU8BA"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== DUST 2 ====================
    elif map_name == "dust2":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== ANCIENT ====================
    elif map_name == "ancient":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== INFERNO ====================
    elif map_name == "inferno":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== CACHE ====================
    elif map_name == "cache":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== ANUBIS ====================
    elif map_name == "anubis":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== OVERPASS ====================
    elif map_name == "overpass":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # ==================== NUKE ====================
    elif map_name == "nuke":
        if position == "a":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "b":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"
        elif position == "mid":
            if grenade_type == "smoke": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "molotov": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "flash": video_id = "СЮДА_АЙДИ"
            elif grenade_type == "he": video_id = "СЮДА_АЙДИ"

    # --- ОТПРАВКА ---
    if video_id and video_id != "СЮДА_АЙДИ":
        await callback.bot.send_video(
            chat_id=callback.message.chat.id,
            video=video_id
        )
    else:
        await callback.message.answer(
            text=f"🎬 Гайд на *{grenade_type.upper()}* ({position.upper()}) для *{map_name.capitalize()}* еще готовится!",
            parse_mode="Markdown"
        )
        
    await callback.answer()


# КНОПКИ НАЗАД

@dp.callback_query(F.data == "back_to_maps")
async def back_to_maps(callback: CallbackQuery):
    await callback.message.edit_text("Выбери карту для раскидки:", reply_markup=maps_kb)

@dp.callback_query(F.data.startswith("back_to_pos_"))
async def back_to_positions(callback: CallbackQuery):
    map_name = callback.data.split("_")[3]
    await callback.message.edit_text(
        text=f"Карта: *{map_name.capitalize()}*\nВыбери часть карты:",
        reply_markup=get_position_kb(map_name),
        parse_mode="Markdown"
    )


import os
from aiohttp import web

async def main():
    print("Бот успешно запущен!")
    
    # Создаем пустышку-сервер, чтобы Render увидел открытый порт
    app = web.Application()
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
