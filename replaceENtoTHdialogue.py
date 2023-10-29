import re

dialog = []
dialog_key = {}
stop = True
with open("dialog_data.txt", "r", encoding="utf-8") as f:
    dialog_data = f.readlines()
    for d in dialog_data:
        x = re.search(r":{{A\|(.*)}} (.*)", d)
        if x:
            dialog_key[x.group(1)] = x.group(2)
with open("dialog.txt", "r", encoding="utf-8") as f:
    dialog = f.readlines()
    for i in range(len(dialog)):
        d = dialog[i]
        x = re.search(r":{{A\|(.*)}} (.*)", d)
        if x:
            if x.group(1) in dialog_key:
                dialog[i] = d.replace(x.group(2), dialog_key[x.group(1)])
        elif not stop:
            y = re.search(r"[\u0E00-\u0E7F]+", d)
            if not y and d not in ("\n", "----\n"):
                if "==" in d:
                    stop = True
                else:
                    dialog[i] = dialog[i].replace("\n","") + "<!-- CHECK ME PLEASE -->\n"
        elif stop:
            if d == "{{Dialogue start}}\n":
                stop = False
        dialog[i] = dialog[i].replace("'''(Traveler):'''", "'''(นักเดินทาง):'''")

with open("dialog_result.txt", "w", encoding="utf-8") as f:
    f.writelines(dialog)