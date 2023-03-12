from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU, LEXICON_CATEGORIES_RU


""" This is keyboard general purpos"""
go_back : KeyboardButton = KeyboardButton(text=LEXICON_RU['back_to_main'])

""" This keyboard will be used for start command """
scrap_info : KeyboardButton = KeyboardButton(text=LEXICON_RU['scrap_info'])

start_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
start_keyboard_bilder.row(
    scrap_info,
    width=3
)
start_keyboard : ReplyKeyboardMarkup = start_keyboard_bilder.as_markup(resize_keyboard=True,)

""" This keyboard will be used for create srap bot """
pepper_scrap : KeyboardButton = KeyboardButton(text=LEXICON_RU['pepper_scrap'])

scrap_keyboard_dilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
scrap_keyboard_dilder.row(
    pepper_scrap,
    go_back,
    width=3
)
scrap_keyboard : ReplyKeyboardMarkup = scrap_keyboard_dilder.as_markup(resize_keyboard=True,)

""" This keyboard will be used from get information about Pepper.ru scraper """

get_information : KeyboardButton = KeyboardButton(text=LEXICON_RU['get_information'])
get_fresh_info : KeyboardButton = KeyboardButton(text=LEXICON_RU['get_fresh_informations'])

managment_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
managment_keyboard_bilder.row(
    get_information,
    get_fresh_info,
    go_back,
    width=2
)
managment_keyboard : ReplyKeyboardMarkup = managment_keyboard_bilder.as_markup(resize_keyboard=True,)

# This keyboard will be used from select categories to get_information services
electronics : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['electronics']}")
gaming : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['gaming']}")
home_and_garden : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['home-and-garden']}")
fashion : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['fashion']}")
health_beauty : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['health-beauty']}")
services : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['services']}")
groceries : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['groceries']}")
family : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['family']}")
sports : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['sports']}")
diy : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['diy']}")
entertainment : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['entertainment']}")
car_motorcycle : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['car-motorcycle']}")
freebies : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['freebies']}")
laptop : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_get_info']}{LEXICON_CATEGORIES_RU['laptop']}")

get_categories_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
get_categories_keyboard_bilder.row(
    electronics,
    gaming,
    home_and_garden,
    fashion,
    health_beauty,
    services,
    groceries,
    family,
    sports,
    diy,
    entertainment,
    car_motorcycle,
    freebies,
    laptop,
    go_back,
    width=2
)

get_categories_keyboard = get_categories_keyboard_bilder.as_markup(resize_keyboard=True, one_time_keyboard=True)



# This keyboard will be used from select categories to get_fresh_information services
electronics : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['electronics']}")
gaming : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['gaming']}")
home_and_garden : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['home-and-garden']}")
fashion : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['fashion']}")
health_beauty : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['health-beauty']}")
services : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['services']}")
groceries : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['groceries']}")
family : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['family']}")
sports : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['sports']}")
diy : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['diy']}")
entertainment : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['entertainment']}")
car_motorcycle : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['car-motorcycle']}")
freebies : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['freebies']}")
laptop : KeyboardButton = KeyboardButton(text=f"{LEXICON_RU['start_part_in_fresh_info']}{LEXICON_CATEGORIES_RU['laptop']}")

get_fresh_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
get_fresh_keyboard_bilder.row(
    electronics,
    gaming,
    home_and_garden,
    fashion,
    health_beauty,
    services,
    groceries,
    family,
    sports,
    diy,
    entertainment,
    car_motorcycle,
    freebies,
    laptop,
    go_back,
    width=2
)

get_fresh_keyboard = get_fresh_keyboard_bilder.as_markup(resize_keyboard=True, one_time_keyboard=True)