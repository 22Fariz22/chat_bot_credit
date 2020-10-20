# -*- coding: utf-8 -*-
import telebot
# 1391358816:AAFCQLtieoSlxYmdNdOFZ4eIhEGWKoju3T4
import telebot

bot = telebot.TeleBot('вставить свой токен')
sum_credit = 0

phone_num = {'89167345200':'Уважаемая Екатерина Юрьевна!', '89288167447': 'Уважаемый Денис Олегович!','89262682738': 'Уважаемый Фариз Фазилевич!'}
client_number = ''
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "введите команду /credit")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == '/credit':
        bot.send_message(message.from_user.id, "Здравствуйте! Пожалуйста введите свой телефонный номер в любом формате")
        bot.register_next_step_handler(message, reg_name)
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

bot.polling()


