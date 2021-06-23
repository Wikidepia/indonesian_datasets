import yyjson
from glob import glob
import esm
import fasttext

banned_word = [
    "xxx",
    "lotto",
    "poker",
    "porn",
    "bokep",
    "judi",
    "sange",
    "togel",
    "memek",
    "kontol",
    "dientot",
    "qiuqiu",
    "betting",
    "taruhan",
    "cock",
    "toket",
    "video jav",
    "video porn",
    "pussy",
    "domino",
    "blowjob",
    "cerita seks",
    "cerita sex",
    "teen sex",
    "milf",
    "doggy style",
    "squirt",
    "fuck",
    "hentai",
    "cumshot",
    "rape",
    "colmek",
    "coli",
    "masturb",
    "tetek",
    "entot",
    "diperkosa",
    "bispak",
    "nyepong",
    "sepong",
    "jablay",
    "ngewe",
    "jilbab hot",
    "lonte",
    "fortamen",
    "vimax",
    "vig power",
    "ceritasex",
    "cerita dewasa",
    "sabung ayam",
    "agen bola",
    "bugil"
]
banned_domain_index = esm.Index()
for domain in banned_word:
    banned_domain_index.enter(domain)
banned_domain_index.fix()


def preprocess_for_fasttext(x):
    return x.replace("\n", " ").replace("\r", " ")[:4000][-1500:]


model = fasttext.load_model("nsfw_filter.bin")
for file in glob("*.json-clean"):
    print(f"-> Processing {file}")
    out = open(file + "-nobet-porn-agc", "a")
    with open(file, "rb") as f:
        for line in f:
            line = line.strip()
            doc = yyjson.loads(line)
            url = doc["url"].lower()
            text = doc["text"].lower()
            qline = banned_domain_index.query(line.decode("utf-8").lower())
            if not (
                len(qline) > 5
                or any( # Spammy domain
                    x in url
                    for x in (
                        "/search/",
                        "/page/",
                        "?q=",
                        "?search=",
                        "s=",
                        ".space",
                        ".icu",
                        "/tag/"
                    )
                ) or any(x in text for x in ("search result", "sites directory")) # SEO Optimization stuff (bad content)
            ):
                out.write(line.decode("utf-8") + "\n")
                continue

            if bool(qline):
                nsfw = model.predict(preprocess_for_fasttext(text))
                if nsfw[0][0] == "__label__sfw":
                    out.write(line.decode("utf-8") + "\n")
