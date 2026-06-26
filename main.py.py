import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from aiohttp import web

# Вставь сюда токен своего основного бота
TOKEN = "8798897292:AAEYTvCge56ry1UPFDHW9QLBXM7gofQ9y60"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# ХЕНДЛЕРЫ
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("👋 Привет! Бот успешно запущен.\n\nВведите команду /menu, чтобы открыть меню выбора карт.")

@dp.message(Command("menu"))
async def menu_cmd(message: types.Message):
    await message.answer("Выбери карту для просмотра раскидок:", reply_markup=get_maps_keyboard())

# ================= БАЗА ДАННЫХ ВСЕХ КАРТ =================
# Просто вставляй ID видео внутрь скобок [], например: ["ID_1", "ID_2"]
GRENADES_DATA = {
    "mirage": {
        "a": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []}
    },
    "inferno": {
        "a": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []}
    },
    "overpass": {
        "a": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []}
    },
    "ancient": {
        "a": {"smoke": ["BAACAgIAAxkBAAN_aj6AwjSygzzAXgYEC5egMQpgScAAAiCiAAP9-EmKCZ2dGQAB4Ds8BA"], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": ["BAACAgIAAxkBAAMEaj6Ho3ghPWxXRQo-iEQweJ8VQ2cAAh6eAAIxuvlJoRXgayF3y1M8BA"], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": ["BAACAgIAAxkBAAMGaj6P4rmhMZrkpR4vZHozGXOeuKQAAo-eAAIxuvlJn8NUQrCj7Og8BA"], "flash": [], "molotov": [], "he": [], "popflash": []}
    },
    "anubis": {
        "a": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []}
    },
    "nuke": {
        "a": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []} # Для Nuke это улица
    },
    "dust2": {
        "a": {"smoke": [], "flash": [], "molotov": ["BAACAgIAAxkBAAMIaj6RevB5dNr_9YJ94rdGRjrNK9oAApSeAAIxuvlJk267PLK_q2I8BA"], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []}
    },
    "cache": {
        "a": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "b": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []},
        "mid": {"smoke": [], "flash": [], "molotov": [], "he": [], "popflash": []}
    }
}

# Красивые названия для вывода в сообщениях
MAP_NAMES = {
    "mirage": "Mirage 🏜️", "inferno": "Inferno 🌋", "overpass": "Overpass 🏙️",
    "ancient": "Ancient 🌴", "anubis": "Anubis 🏛️", "nuke": "Nuke 🏭",
    "dust2": "Dust 2 🕌", "cache": "Cache 🟢"
}
POSITION_NAMES = {"a": "Плент А 🅰️", "b": "Плент Б 🅱️", "mid": "Мидл/Улица ↩️"}
GRENADE_NAMES = {
    "smoke": "Смок 💨", "flash": "Флешка 👁️", "molotov": "Молотов 🔥", 
    "he": "ХАЕшка 💥", "popflash": "Моменталка ⚡"
}

# Генерирует клавиатуру выбора карт (по 2 в ряд)
def get_maps_keyboard():
    buttons = [
        [InlineKeyboardButton(text="Mirage 🏜️", callback_data="map_mirage"), InlineKeyboardButton(text="Inferno 🌋", callback_data="map_inferno")],
        [InlineKeyboardButton(text="Overpass 🏙️", callback_data="map_overpass"), InlineKeyboardButton(text="Ancient 🌴", callback_data="map_ancient")],
        [InlineKeyboardButton(text="Anubis 🏛️", callback_data="map_anubis"), InlineKeyboardButton(text="Nuke 🏭", callback_data="map_nuke")],
        [InlineKeyboardButton(text="Dust 2 🕌", callback_data="map_dust2"), InlineKeyboardButton(text="Cache 🟢", callback_data="map_cache")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ================= ШАГ 1: СТАРТ / ВЫБОР КАРТЫ =================
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("👋 Привет! Выбери карту для просмотра раскидок:", reply_markup=get_maps_keyboard())

# ================= ШАГ 2: ВЫБОР ТОЧКИ =================
@dp.callback_query(F.data.startswith("map_"))
async def select_position(callback: types.CallbackQuery):
    map_name = callback.data.split("_")[1]
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Плент А 🅰️", callback_data=f"pos_{map_name}_a")],
        [InlineKeyboardButton(text="Плент Б 🅱️", callback_data=f"pos_{map_name}_b")],
        [InlineKeyboardButton(text="Мидл / Улица ↩️", callback_data=f"pos_{map_name}_mid")],
        [InlineKeyboardButton(text="⬅️ Назад к картам", callback_data="back_maps")]
    ])
    await callback.message.edit_text(f"Выбрана карта: **{MAP_NAMES.get(map_name)}**\nТеперь выбери позицию:", parse_mode="Markdown", reply_markup=keyboard)

# ================= ШАГ 3: ВЫБОР ТИПА ГРАНАТЫ =================
@dp.callback_query(F.data.startswith("pos_"))
async def select_grenade_type(callback: types.CallbackQuery):
    _, map_name, pos_name = callback.data.split("_")
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Смок 💨", callback_data=f"type_{map_name}_{pos_name}_smoke"), InlineKeyboardButton(text="Флешка 👁️", callback_data=f"type_{map_name}_{pos_name}_flash")],
        [InlineKeyboardButton(text="Молотов 🔥", callback_data=f"type_{map_name}_{pos_name}_molotov"), InlineKeyboardButton(text="ХАЕшка 💥", callback_data=f"type_{map_name}_{pos_name}_he")],
        [InlineKeyboardButton(text="Моменталка ⚡", callback_data=f"type_{map_name}_{pos_name}_popflash")],
        [InlineKeyboardButton(text="⬅️ Назад к позициям", callback_data=f"map_{map_name}")]
    ])
    await callback.message.edit_text(
        f"Карта: **{MAP_NAMES.get(map_name)}** | Позиция: **{POSITION_NAMES.get(pos_name)}**\nВыбери тип гранаты:", 
        parse_mode="Markdown", reply_markup=keyboard
    )

# ================= ШАГ 4: МЕНЮ С ЦИФРАМИ =================
@dp.callback_query(F.data.startswith("type_"))
async def show_grenade_variants(callback: types.CallbackQuery):
    _, map_name, pos_name, gren_type = callback.data.split("_")
    
    videos = GRENADES_DATA.get(map_name, {}).get(pos_name, {}).get(gren_type, [])
    
    if not videos:
        await callback.answer("⚠️ Для этой точки видео еще не загружены!", show_alert=True)
        return

    buttons = []
    row = []
    for index, _ in enumerate(videos, start=1):
        row.append(InlineKeyboardButton(text=f"Вариант {index} 🎥", callback_data=f"video_{map_name}_{pos_name}_{gren_type}_{index-1}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
        
    buttons.append([InlineKeyboardButton(text="⬅️ Назад к гранатам", callback_data=f"pos_{map_name}_{pos_name}")])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.message.edit_text(
        f"Карта: **{MAP_NAMES.get(map_name)}**\nПозиция: **{POSITION_NAMES.get(pos_name)}**\nТип: **{GRENADE_NAMES.get(gren_type)}**\n\nВыбери номер раскидки:",
        parse_mode="Markdown", reply_markup=keyboard
    )

# ================= ШАГ 5: ОТПРАВКА ВИДЕО =================
@dp.callback_query(F.data.startswith("video_"))
async def send_grenade_video(callback: types.CallbackQuery):
    _, map_name, pos_name, gren_type, video_index = callback.data.split("_")
    video_index = int(video_index)
    
    videos = GRENADES_DATA.get(map_name, {}).get(pos_name, {}).get(gren_type, [])
    
    if video_index < len(videos):
        video_id = videos[video_index]
        caption_text = f"🎬 {MAP_NAMES.get(map_name)} | {POSITION_NAMES.get(pos_name)} | {GRENADE_NAMES.get(gren_type)} (Вариант {video_index+1})"
        
        await callback.message.answer_video(video=video_id, caption=caption_text)
        await callback.answer("Видео отправлено!")
    else:
        await callback.answer("Ошибка: видео не найдено.", show_alert=True)

# ================= КНОПКА НАЗАД В МЕНЮ КАРТ =================
@dp.callback_query(F.data == "back_maps")
async def back_to_maps(callback: types.CallbackQuery):
    await callback.message.edit_text("Выбери карту для просмотра раскидок:", reply_markup=get_maps_keyboard())

# ================= КОД ДЛЯ ОБМАНА RENDER (ВЕБ-СЕРВЕР) =================
async def handle_root(request):
    return web.Response(text="Бот работает!")

async def start_webserver():
    app = web.Application()
    app.router.add_get('/', handle_root)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Микро-сервер запущен на порту {port}")

async def main():
    # Вот эту строчку добавляем:
    await start_webserver()
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
