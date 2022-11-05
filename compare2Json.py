
#This script will remove any empty items in json file, That's useful for Data Mining with Genshin Impact dialogue.

import json

# Change your target json file here
file1 = "TextMap/302_TextMapTH.json"
file2 = "TextMap/301_TextMapTH.json"

data1,data2 = {}, {}
with open(file1, "r", encoding="utf-8") as f:
    data1 = json.load(f)
with open(file2, "r", encoding="utf-8") as f:
    data2 = json.load(f)

data3 = {}
for i in data2:
    if (i in data1) and (data2[i] != data1[i]):
        data3[i] = {"3.1": data1[i], "3.2": data2[i]}

with open(f"compared.json", "w", encoding="utf-8") as f:
    json.dump(data3, f, sort_keys=True, indent=4, ensure_ascii=False)
    f.close()
    print("Wrote file.")
