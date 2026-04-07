import csv
import os
import yt_dlp

liste = []

with open("music.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        liste.append([row["Song"], row["Artist"]])

os.makedirs("music", exist_ok=True)

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "music/%(title)s.%(ext)s",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",
    }],
    "quiet": False
}

for musique, artiste in liste:

    query = f"{artiste} - {musique}"

    print(f"Téléchargement : {query}")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{query}"])