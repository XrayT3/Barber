import telebot
import const
import markups
import time
import base
from telebot import types

bot = telebot.TeleBot(const.token)


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id in const.admins:
        markup = markups.start_admin()
    else:
        markup = markups.start()
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '!', reply_markup=markup)
    base.add_user(message)


@bot.message_handler(content_types=['text'])
def zvonki(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn_user = telebot.types.InlineKeyboardButton(text="Вконтакте", url="vk.com/barberkontorachel")
    btn_celler = telebot.types.InlineKeyboardButton(text="Инстаграм", url="instagram.com/kontora.chel/")
    markup.add(btn_celler, btn_user)

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('НАЗАД')

    if message.text == 'О нас':
        bot.send_message(message.chat.id, const.about, parse_mode='HTML')

    if message.text == 'Услуги':
        bot.send_message(message.chat.id, const.amenities, parse_mode='HTML')

    if message.text == 'Контакты':
        bot.send_message(message.chat.id, const.contactus,
                         parse_mode='HTML', reply_markup=markup)

    if message.text == 'Рассылка':
        msg = bot.send_message(message.chat.id, "Введите текст, который хотите отправить всем не клиентам", reply_markup=keyboard)
        bot.register_next_step_handler(msg, send_to_users)


def send_to_users(message):
    if message.text.upper() == "НАЗАД":
            bot.send_message(message.chat.id, "Отменено", reply_markup=markups.start_admin())
            return
    else:
            count = 0
            for user in base.get_all_users():
                #if user[8] == 'FALSE':
                    count += 1
                    print(count)
                    if user[1] == const.admins:
                        continue
                    if count % 20 == 0:
                        time.sleep(1)
                    try:
                        bot.send_message(user[1], message.text)
                        print("message sent to %s count = %s" % (user[4], count))
                    except Exception as e:
                        continue
            bot.send_message(message.chat.id, "Сообщение успешно отправлено всем !",
                             reply_markup=markups.start_admin())

bot.polling()
