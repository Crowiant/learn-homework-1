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
    planet_dict = {
        'Mars': ephem.Mars,
        'Jupiter': ephem.Jupiter,
        'Mercury': ephem.Mercury,
        'Venus': ephem.Venus,
        'Saturn': ephem.Saturn,
        'Uranus': ephem.Uranus,
        'Neptune': ephem.Neptune,
    }
    dt_now = ephem.now()
    get_planet = update.message.text.split()
    if planet_dict.get(get_planet[1]):
        planet_name = planet_dict.get(get_planet[1])
        planet_name = planet_name(dt_now)
        planet_constellation = ephem.constellation(planet_name)
        update.message.reply_text(planet_constellation[1])
    else:
        update.message.reply_text('Про этот объект я ничего не знаю')


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
