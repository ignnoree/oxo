from logic import bot
from logic import send_welcome
from logic import mainfunc



@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    send_welcome()

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    mainfunc(message)

bot.polling()