from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon_ru import LEXICON_RU


""" This keyboard will be used for start command"""
game_botton : KeyboardButton = KeyboardButton(text=LEXICON_RU['start_game'])

start_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
start_keyboard_bilder.row(
    game_botton,
    width=3
)
start_keyboard : ReplyKeyboardMarkup = start_keyboard_bilder.as_markup(resize_keyboard=True,)
""" This keyboard will be used for playing in rock, scissors and paper"""
# Create Yes/No button
button_yes : KeyboardButton = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no : KeyboardButton = KeyboardButton(text=LEXICON_RU['no_button'])
back_botton : KeyboardButton = KeyboardButton(text=LEXICON_RU['back_to_main'])
# Create variables button
button_1 : KeyboardButton = KeyboardButton(text=LEXICON_RU['rock'])
button_2 : KeyboardButton = KeyboardButton(text=LEXICON_RU['scissors'])
button_3 : KeyboardButton = KeyboardButton(text=LEXICON_RU['paper'])

yes_no_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
yes_no_keyboard_bilder.row(button_yes, button_no, back_botton, width=2)

yes_no_keyboard : ReplyKeyboardMarkup = yes_no_keyboard_bilder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

game_keyboard_bilder : ReplyKeyboardBuilder = ReplyKeyboardBuilder()
game_keyboard_bilder.row(button_1, button_2, button_3, width=3)

game_keyboard : ReplyKeyboardMarkup = game_keyboard_bilder.as_markup(
    resize_keyboard=True
)