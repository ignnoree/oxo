from .config import bot 
from .download_logic import download_song
import os




def playlist_handler(message):
    args = message.text.split(maxsplit=1)  
    if not len(args) > 1:
        bot.reply_to(message, "Where is the link !, = /p https://...")

    link_after_command = args[1]  
    download_song(link_after_command)
    
    script_dir = os.path.dirname(os.path.realpath(__file__))
    music_folder = os.path.join(script_dir, 'musics')
    mp3_files = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]

    for f in mp3_files:
        full_file_path = os.path.join(music_folder, f)
        bot.send_audio(message.chat.id, open(full_file_path, 'rb'))  # Open in 'rb' here automatically
        os.remove(full_file_path) 
    
   
    
    


