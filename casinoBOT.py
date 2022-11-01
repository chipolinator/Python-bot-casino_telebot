import telebot

import random
from telebot import types

bot = telebot.TeleBot("5424302646:AAEldtAqN1xA_iIhYj9ppV7253jTcIsPRjI")
summ = 500


@bot.message_handler(commands=["start"])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    casino = types.KeyboardButton("/casino")
    markup.add(casino)

    mess = f'Привет, пользователь! Ладно, шучу. Я знаю что ты <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id, mess, parse_mode="html", reply_markup = markup)

    if message.from_user.username=="ShiningLeafu":
        bot.send_message(message.chat.id, "мыслант гигысли и таинственный шляпник. грандмастер программёр. хаха это личная приписка по нику. почувствуй себя ✨особенным✨")
    elif message.from_user.username=="i_found_u":
        bot.send_message(message.chat.id, "проверка сообщения по нику")


@bot.message_handler(commands=["casino"])
def casino(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Орел", callback_data='0')
    btn2 = types.InlineKeyboardButton("Решка", callback_data='1')
    markup.add(btn1, btn2)
    if summ > 0:
        bot.send_message(message.chat.id, 'Давай, игроман, оставь своих детей без ужина', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Неа, ты свой шанс уже потерял', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton("Орел", callback_data='0')
            btn2 = types.InlineKeyboardButton("Решка", callback_data='1')
            markup.add(btn1, btn2)

            global summ
            num = str(random.randint(0, 1))
            if summ > 0:
                if (num == "0"):
                    bot.send_message(call.message.chat.id, 'Выпал орел')
                else:
                    bot.send_message(call.message.chat.id, 'Выпала решка')
                if (num == call.data):
                    summ += 500
                    bot.send_message(call.message.chat.id, '🎉🎉🎉ПОБЕДА🎉🎉🎉 \nу тебя '+str(summ)+" рублей", parse_mode="html", reply_markup=markup)
                else:
                    summ -= 500
                    bot.send_message(call.message.chat.id, '🎰🎰🎰ПРОИГРЫШ🎰🎰🎰 \nу тебя '+str(summ)+" рублей", parse_mode="html", reply_markup=markup)
            else:
                bot.send_message(call.message.chat.id, "Поздравляю! Ты остался без денег!")

    except Exception as e:
        print(repr(e))


@bot.message_handler()
def ans(message):
    markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Я для кого варианты ответов писала?", reply_markup = markup)

bot.polling(none_stop=True)
