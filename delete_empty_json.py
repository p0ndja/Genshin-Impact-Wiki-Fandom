
#This script will remove any empty items in json file, That's useful for Data Mining with Genshin Impact dialogue.

import json

# Change your target json file here
file = "TextMapCHS.json"

data = {}
with open(file, "r", encoding="utf-8") as f:
    data = json.load(f)

key_to_remove = []

for i in data:
    if not len(data.get(i)):
        key_to_remove.append(i)

for i in key_to_remove:
    data.pop(i)

with open("minify_"+str(file), "w", encoding="utf-8") as f:
    json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)
    f.close()