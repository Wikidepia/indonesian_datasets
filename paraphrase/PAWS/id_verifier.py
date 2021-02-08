import pandas as pd

id_datas = pd.read_csv("data/test_translated.tsv", sep="\t")
id_list = list(id_datas["id"])
for i in range(1, 8001):
    if i not in id_list:
        print(i)
