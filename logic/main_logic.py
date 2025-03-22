import telebot
from .download_logic import download_song
from logic.messages.messages import messages,illegal_download_messages,welcome_messages
from .api.apis import bot_api
import random
import os
import re

spotify_link_pattern = re.compile(r'https://open\.spotify\.com/track/')

bot = telebot.TeleBot(bot_api, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message,random.choice(welcome_messages))

	

@bot.message_handler(func=lambda m: True)
def mainfunc(message):
    link=message.text

    if not spotify_link_pattern.match(link):
        bot.reply_to(message, f"That's not a valid Spotify link! Please send a valid link to a track. Also {random.choice(illegal_download_messages)}")
        return  

    processing_message=bot.reply_to(message, random.choice(messages))

    download_song(link)
    
    current_directory = os.path.dirname(os.path.abspath(__file__))
    parent_directory = os.path.dirname(current_directory)

    files = os.listdir(parent_directory)

    music_file = next((f for f in files if f.endswith('.mp3')), None)

    if music_file:
        


            
            with open(music_file, 'rb') as file:
                bot.send_audio(message.chat.id, file)
            
            
            os.remove(music_file)

        
    bot.delete_message(message.chat.id, processing_message.message_id)
    processing_message=bot.reply_to(message, random.choice(illegal_download_messages))
    

    

 


bot.infinity_polling()