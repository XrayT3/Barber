import telebot


def start():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('О нас', 'Услуги')
    keyboard.row('Контакты')
    return keyboard


def start_admin():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('О нас', 'Услуги')
    keyboard.row('Контакты')
    keyboard.row('Рассылка')
    return keyboard
