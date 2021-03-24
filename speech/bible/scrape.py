import requests
import json
import os
import multiprocessing

from functools import partial


def dl(chapter, book_id):
    # You need to get this manually from view-source:https://live.bible.is/bible/INDWBT/MAT/1?audio_type=audio_drama
    VERSE_ID = "INDWBT"
    AUDIO_ID = "INZTSIN2DA"
    if os.path.exists(f"sederhana_dramatized/{book_id}/{chapter}.mp3") and os.path.exists(
        f"sederhana_dramatized/{book_id}/{chapter}.txt"
    ):
        return
    verse_text = ""
    verse_url = f"https://api.v4.dbt.io/bibles/filesets/{VERSE_ID}/{book_id}/{chapter}?key=52e62d4c-f7c8-4a8b-9008-8634d0fbddb0&v=4"
    audio_url = f"https://api.v4.dbt.io/bibles/filesets/{AUDIO_ID}?asset_id=dbp-prod&key=52e62d4c-f7c8-4a8b-9008-8634d0fbddb0&v=4&book_id={book_id}&chapter_id={chapter}&type=audio_drama"

    verses = requests.get(verse_url).json()
    audio = requests.get(audio_url).json()
    if "error" in audio:
            if "error" in audio:
                print(chapter, book_id, audio)
                return
    assert len(audio["data"]) == 1
    audio_url = audio["data"][0]["path"]
    for verse in verses["data"]:
        verse_text += verse["verse_text"] + " "
    dl_audio = requests.get(audio_url)
    with open(f"sederhana_dramatized/{book_id}/{chapter}.mp3", "wb") as f:
        f.write(dl_audio.content)
    with open(f"sederhana_dramatized/{book_id}/{chapter}.txt", "w") as f:
        f.write(verse_text)
    print("Downloaded", book_id, chapter)


if __name__ == "__main__":
    with open("sederhana.json") as f:
        info = json.load(f)
    for booki in info:
        book_id = booki["book_id"]
        os.makedirs(f"sederhana_dramatized/{book_id}", exist_ok=True)
        pool = multiprocessing.Pool(1)
        chapters = booki["chapters"]
        results = pool.map(partial(dl, book_id=book_id), chapters)
        pool.close()
        pool.join()
