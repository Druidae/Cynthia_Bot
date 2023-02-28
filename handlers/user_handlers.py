from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Text

from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import yes_no_keyboard, game_keyboard, start_keyboard
from services.services import get_bot_choise, get_winner


router : Router = Router()

# Triggered by /start command
@router.message(CommandStart())
@router.message(Text(text=LEXICON_RU['back_to_main']))
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_keyboard)

# Triggered by /help command
@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# Triggered by /game command
@router.message(Command(commands=['game']))
@router.message(Text(text=LEXICON_RU['start_game']))
async def process_game_command(message: Message):
    await message.answer(text=LEXICON_RU['/game'], reply_markup=yes_no_keyboard)
# Triggered when user send yes
@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_unswer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_keyboard)

# Triggered when user send no
@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_unswer(message: Message):
    await message.answer(text=LEXICON_RU['no'], reply_markup=yes_no_keyboard)

# Triggered by any game botton
@router.message(Text(text=[LEXICON_RU['rock'], LEXICON_RU['paper'], LEXICON_RU['scissors']]))
async def game_process(message: Message):
    bot_choice = get_bot_choise()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]}-{LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_keyboard)