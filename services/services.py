import random

from lexicon.lexicon_ru import LEXICON_RU


def get_bot_choise() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

def _normalize_user_unswer(user_unswer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_unswer:
            return key
    raise Exception

def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_unswer(user_choice)
    rules : dict[str, str] = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'