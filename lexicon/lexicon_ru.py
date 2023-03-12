LEXICON_RU : dict[str, str] = {
    '/start': '<b>Cithia приветствует тебя <i>странник</i>,\nчем я могу помочь тебе?</b>\nБольше информации о моих способностях по команде /help',
    '/help': 'Это очень простая игра. Мы одновременно должны '
             'сделать выбор одного из трех предметов. Камень, '
             'ножницы или бумага.\n\nЕсли наш выбор '
             'совпадает - ничья, а в остальных случаях камень '
             'побеждает ножницы, ножницы побеждают бумагу, '
             'а бумага побеждает камень.\n\n<b>Играем?</b>',
    '/game': '<b>Привет!</b>\nДавай с тобой сыграем в игру '
              '"Камень, ножницы, бумага"?\n\nЕсли ты, вдруг, '
              'забыл правила, команда /help тебе поможет!\n\n<b>Играем?</b>',

    'scrap_info': "Доступные магазины",
    'pepper_scrap': "Магазин Pepper.ru",

    'get_information': "Получить инфрмацию о таварах",
    'get_fresh_informations': "Получить инфомацию о новых товарах",
    'select_categories': 'Выберете категорию товара',
    'select_services': 'Выберете необходимую операцию',

    'back_to_main': 'Вернутья в главное меню',

    'start_part_in_get_info': 'Поиск в категории: ',
    'start_part_in_fresh_info': 'Новинки в категории: ',
    'no_fresh': 'Новые товары отсутсвуют',
    'other_answer': 'Извини, увы, это сообщение мне непонятно...',

}

LEXICON_COMMANDS_RU: dict[str, str] = {
                '/start': 'Запуск бота',
                '/help': 'Here you can find more information',
                '/command_3': 'command_3 desription',
                '/command_4': 'command_4 desription'
}

""" Categories from Pepper.ru  to """
LEXICON_CATEGORIES_RU : dict[str, str] = {
    "electronics" : "Электроника",
    "gaming" : "Консоли и Видеоигры",
    "home-and-garden" : "Дом и Квартира",
    "fashion" : "Мода",
    "health-beauty" : "Здоровье и Красота",
    "services" : "Услуги и Подписки",
    "groceries" : "Продукты питания и Бытовая химия",
    "family" : "Семья и Дети",
    "sports" : "Спорт и Активный отдых",
    "diy" : "Ремонт и Строительство",
    "entertainment" : "Культура и Отдых",
    "car-motorcycle" : "Автомобили",
    "freebies" : "Бесплатно",
    "laptop" : "Ноутбуки"
}

LEXICON_URL_CATEGORIES_RU : dict[str, str] = {
    "Электроника": "electronics",
    "Консоли и Видеоигры": "gaming",
    "Дом и Квартира": "home-and-garden",
    "Мода": "fashion",
    "Здоровье и Красота": "health-beauty",
    "Услуги и Подписки": "services",
    "Продукты питания и Бытовая химия": "groceries",
    "Семья и Дети": "family",
    "Спорт и Активный отдых": "sports",
    "Ремонт и Строительство": "diy",
    "Культура и Отдых": "entertainment",
    "Автомобили": "car-motorcycle",
    "Бесплатно": "freebies",
    "Ноутбуки": "laptop"
}