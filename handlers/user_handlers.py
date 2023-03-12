import json
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, Text
from aiogram.utils.markdown import hbold, hunderline, hlink, hcode

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_URL_CATEGORIES_RU
from keyboards.keyboards import start_keyboard, scrap_keyboard, managment_keyboard, get_categories_keyboard, get_fresh_keyboard
from external_services.scrap.pepper_ru.selenium_module import get_fresh_page


router : Router = Router()

# Triggered by /start command
@router.message(CommandStart())
@router.message(Text(text=LEXICON_RU['back_to_main']))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_keyboard)

@router.message(Text(text=LEXICON_RU['scrap_info']))
async def process_scrap_command(message: Message):
    await message.answer(text=LEXICON_RU['scrap_info'],reply_markup=scrap_keyboard)

@router.message(Text(text=LEXICON_RU['pepper_scrap']))
async def process_scrap_command(message: Message):
    await message.answer(text=LEXICON_RU['select_services'],reply_markup=managment_keyboard)

@router.message(Text(text=LEXICON_RU['get_information']))
async def process_get_info_command(message: Message):
    await message.answer(text=LEXICON_RU['select_categories'],reply_markup=get_categories_keyboard)


@router.message(Text(text=LEXICON_RU['get_fresh_informations']))
async def process_get_info_command(message: Message):
    await message.answer(text=f"{LEXICON_RU['select_categories']}",reply_markup=get_fresh_keyboard)

@router.message(Text(startswith=f"{LEXICON_RU['start_part_in_fresh_info']}"))
async def process_get_fresh_items(message: Message):
    categories : str = message.text.split(':')[-1].strip()
    await message.answer(text=f"Поиск новинок в категории: {categories}\nПожалуйта ожидайте...")
    fresh_items = get_fresh_page(categories=LEXICON_URL_CATEGORIES_RU[categories])

    if len(fresh_items) >= 1:
        for k, v in sorted(fresh_items.items()):
            items = f"{hlink(v['item_name'], v['item_url'])}\n" \
                    f"{hbold(v['item_price'])}\n" \
                # f"{hunderline(v['item_name'])}\n" \
            await message.answer(items)
    else:
        await message.answer(text=LEXICON_RU['no_fresh'])

@router.message(Text(startswith=f"{LEXICON_RU['start_part_in_get_info']}"))
async def process_get_all_items(message: Message):
    categories : str = message.text.split(':')[-1].strip()

    with open(f'data/pepper_ru_scrap/output_data/{LEXICON_URL_CATEGORIES_RU[categories]}_result.json', 'r') as file:
        items_dict : dict = json.load(file)

    for k, v in sorted(items_dict.items()):
        items = f"{hlink(v['item_name'], v['item_url'])}\n" \
                f"{hbold(v['item_price'])}\n" \
                # f"{hunderline(v['item_name'])}\n" \

        await message.answer(items)

# Triggered by /help command
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
