from .download_logic import download_song
from logic.messages.messages import messages,illegal_download_messages,welcome_messages
import random
import os
from .config import bot,spotify_link_pattern


def send_welcome(message):
	bot.reply_to(message,random.choice(welcome_messages))

	
user_locks = {}

def mainfunc(message):
    user_id = message.chat.id
    

    if user_id in user_locks and user_locks[user_id]:
        bot.reply_to(message, "Your previous request is still being processed. Please wait...")
        return

    
    user_locks[user_id] = True

    link = message.text

    if not spotify_link_pattern.match(link):
        bot.reply_to(message, f"That's not a valid Spotify link! Please send a valid link to a track. Also {random.choice(illegal_download_messages)}")
        user_locks[user_id] = False 
        return

    processing_message = bot.reply_to(message, random.choice(messages))

    download_song(link)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    music_folder = os.path.join(script_dir, 'musics')
    mp3_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

    for f in mp3_files:
        full_file_path = os.path.join(music_folder, f)
        bot.send_audio(message.chat.id, open(full_file_path, 'rb')) 
        os.remove(full_file_path)

    bot.delete_message(message.chat.id, processing_message.message_id)
    bot.reply_to(message, random.choice(illegal_download_messages))


    user_locks[user_id] = False
    

 
