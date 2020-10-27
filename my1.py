# -*- coding: utf-8 -*-
import telebot
# 1391358816:AAFCQLtieoSlxYmdNdOFZ4eIhEGWKoju3T4
import telebot
from json_write_function import write_json


bot = telebot.TeleBot('тут токен, спросите у меня')
sum_credit = 0

phone_num = {тут список номеров типа '89161234567':'Иван Петров',}
name = ''
client_number = ''
credit = ''
user_id = ''
person = {
    'name': name,
    'phone_number': str(client_number),
    'credit': str(credit),
    'user_id': user_id
    }


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "введите команду /credit")
num = ''
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    global num
    if message.text == '/credit':
        bot.send_message(message.from_user.id, "Здравствуйте! Пожалуйста введите свой телефонный номер в любом формате")
        num = bot.register_next_step_handler(message, reg_name)

        # попробуем вывести и сохранить куда нибудь тел номер

flag = False
def reg_name(message):
    global client_number
    global flag
    # тут надо сделать проверку на isdigit()
    client_number = message.text.replace("-", "").replace(" ", "")[-10:]
    for k, v in phone_num.items():
        if k.replace("-", "").replace(" ", "")[-10:] == client_number:
            print(bot.send_message(message.from_user.id, f"{v},введите сумму не превышающую 100.000 рублей"))
            flag = True
            person['name'] = v
            person['phone_number'] = k

    if flag == False:
        print(bot.send_message(message.from_user.id,"Извините, ваш номер не найден. Вам надо пройти регистрацию"))

    bot.register_next_step_handler(message, reg_sum)

def reg_sum(message):
    global sum_credit
    #ввести проверку на содержание символов
    sum_credit = int(message.text)
    if sum_credit >= 100000:
        bot.send_message(message.from_user.id, "Вы ввели сумму превышающий допустимое значение."
                                              "Попробуйте сначала, введите введите команду /credit")
    else:
        bot.send_message(message.from_user.id, "Ваш запрос отправлен в банк,"
                                              " ожидайте ответа.Спасибо.")
        person['credit'] = str(message.text)

        write_json(person)


bot.polling()

