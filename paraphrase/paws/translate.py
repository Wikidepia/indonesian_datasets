import pandas as pd
from google_trans_new import google_translator
import concurrent.futures as confu

# ID Verifier
# notav_id = open("notav").read().split()
def translate(row):
    sentence1 = row["sentence1"]
    sentence2 = row["sentence2"]
    id_sentence = row["id"]
    label = row["label"]

    # ID Verifier
    """
    if str(id_sentence) not in notav_id:
        return
    """

    # Append all sentences and use separator to reduce API usage and prevent block from Google
    cat_sentence = sentence1 + " [<=>] " + sentence2
    translated_sentence = translator.translate(cat_sentence, lang_src="en", lang_tgt="id")
    print(cat_sentence)
    translated_sentence = translated_sentence.split("[<=>]")
    translated_datas = open("data/test_translated.tsv", "a")

    # Smooth brain code
    translated_datas.write(
        str(id_sentence)
        + "\t"
        + translated_sentence[0].strip()
        + "\t"
        + translated_sentence[1].strip()
        + "\t"
        + str(label)
        + "\n"
    )
    return translated_sentence


if __name__ == "__main__":
    # Use rotating proxy to prevent "429 Too Many Request"
    translator = google_translator(
        proxies={"http": "195.154.255.118:15001", "https": "195.154.255.118:15001"}
    )
    datas = pd.read_csv("data/test.tsv", sep="\t")

    with confu.ThreadPoolExecutor(10) as executor:
        futures = [executor.submit(translate, row) for _, row in datas.iterrows()]
        for future in confu.as_completed(futures):
            try:
                pass
            except ValueError as e:
                print(e)
