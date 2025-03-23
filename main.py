from logic import bot
from logic import send_welcome
from logic import mainfunc
from logic import playlist_handler



@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    send_welcome(message)



@bot.message_handler(commands=['playlist','pl'])
def handle_playlist(message):
    playlist_handler(message)



@bot.message_handler(func=lambda message: not message.text.startswith("/"))
def handle_message(message):
    mainfunc(message)


if __name__=="__main__":
    print("Bot is running...") 
    bot.polling()