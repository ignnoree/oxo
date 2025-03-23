import os
import subprocess

def download_song(song_url):
 
    music_folder = os.path.join(os.getcwd(), 'logic/functions/musics')
    
    
    if not os.path.exists(music_folder):
        os.makedirs(music_folder)
    

    process = subprocess.Popen(
        ["spotdl", song_url, "--output", music_folder],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    
    print(process.stdout)

    for line in process.stdout:
        print(line.strip())

    process.wait()
    if process.returncode == 0:
        print("Download complete!")
    else:
        print("Error occurred!")

