
#This script will remove any empty items in json file, That's useful for Data Mining with Genshin Impact dialogue.

import json

# Change your target json file here
file1 = "minify_205TextMapTH.json"
file2 = "minify_206TextMapTH.json"

data1,data2 = {}, {}
with open(file1, "r", encoding="utf-8") as f:
    data1 = json.load(f)
with open(file2, "r", encoding="utf-8") as f:
    data2 = json.load(f)

data3 = {}
for i in data2:
    if (i not in data1):
        data3[i] = {"old": "", "new": data2[i]}
    elif (data2[i] != data1[i]):
        data3[i] = {"old": data1[i], "new": data2[i]}

with open(f"compare_{file1}{file2}.json", "w", encoding="utf-8") as f:
    json.dump(data3, f, sort_keys=True, indent=4, ensure_ascii=False)
    f.close()
    print("Wrote file.")

duplicate = []
for i in data3:
    for o in data3:
        if data3[i]["new"] is data3[o]["old"]:
            print(f"Duplicate {i} <-> {o}")
            duplicate.append({i,o})
            continue
print(duplicate)
