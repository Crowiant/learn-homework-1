"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)


def find_planet_place(update, context):
    dt_now = ephem.now()
    get_planet = update.message.text.split()
    if get_planet[1] == 'Mars':
        planet_name = ephem.Mars(dt_now)
    if get_planet[1] == 'Jupiter':
        planet_name = ephem.Jupiter(dt_now)
    if get_planet[1] == 'Mercury':
        planet_name = ephem.Mercury(dt_now)
    if get_planet[1] == 'Venus':
        planet_name = ephem.Venus(dt_now)
    if get_planet[1] == 'Saturn':
        planet_name = ephem.Saturn(dt_now)
    if get_planet[1] == 'Uranus':
        planet_name = ephem.Uranus(dt_now)
    if get_planet[1] == 'Neptune':
        planet_name = ephem.Neptune(dt_now)
    else:
        update.message.reply_text('Про этот объект я ничего не знаю')
    planet_constellation = ephem.constellation(planet_name)
    update.message.reply_text(planet_constellation[1])


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', find_planet_place))

    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
