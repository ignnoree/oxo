import subprocess

def download_song(song_url):
    process = subprocess.Popen(["spotdl", song_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print(process.stdout)

    for line in process.stdout:
        print(line.strip())

    process.wait()
    if process.returncode == 0:
        print("Download complete!")
    else:
        print("Error occurred!")

