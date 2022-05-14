
# Format to find "<a href="https://static.wikia.nocookie.net/gensin-impact/images/<File URL>"
# Find from "https://genshin-impact.fandom.com/wiki/File:<File URL>"

# Accept in format:
# - just a file name "Character Kaedehara Kazuha Card.png"
# - a wiki file url "https://genshin-impact.fandom.com/wiki/File:Character_Kaedehara_Kazuha_Card.png"
# - a direct file url "https://static.wikia.nocookie.net/gensin-impact/images/2/2d/Character_Kaedehara_Kazuha_Card.png/revision/latest"

import urllib.request
import urllib.parse
import re
import os.path

def dl(url:str):
    if urlType(url) == 0:
        url = urllib.parse.quote(url.strip().replace("  ", " ").replace(" ", "_"))
        fp = urllib.request.urlopen(f"https://genshin-impact.fandom.com/wiki/File:{url}")
        target = re.findall(f"https:\/\/static.wikia.nocookie.net\/gensin-impact\/images\/[a-zA-Z0-9]\/[a-zA-Z0-9][a-zA-Z0-9]\/{url}\/revision\/latest",fp.read().decode("utf8"))
        fp.close()
    elif urlType(url) == 1:
        fp = urllib.request.urlopen(url)
        olf = urllib.parse.quote(url.replace("https://genshin-impact.fandom.com/wiki/File:", ""))
        target = re.findall(f"https:\/\/static.wikia.nocookie.net\/gensin-impact\/images\/[a-zA-Z0-9]\/[a-zA-Z0-9][a-zA-Z0-9]\/{olf}\/revision\/latest",fp.read().decode("utf8"))
        fp.close()
    elif urlType(url) == 2:
        target = re.findall(f"https:\/\/static.wikia.nocookie.net\/(.*)\/images\/[a-zA-Z0-9]\/[a-zA-Z0-9][a-zA-Z0-9]\/(.*)\/revision\/latest",url)
        url = url.replace("/scale-to-width-down/", "?")

    if len(target) > 0:
        if (urlType(url) == 2):
            file_name = target[0][1]
        else:
            url = target[0]
            file_name = url.split('/')[-3]
        file_name = urllib.parse.unquote(file_name)
        if(urllib.request.urlretrieve(url, f"./download/{file_name}")):
            print("Downloaded", file_name.replace("_", " "))
            
            nam,ext = defineFile(file_name)
            if ext == "gif" and not checkExist(f"{nam}ogv"):
                dl(f"{nam}ogv")
            elif ext == "ogv" and not checkExist(f"{nam}gif"):
                dl(f"{nam}gif")
            
            return 1
    print(f"Unable to download {url}")
    return 0

def urlType(url:str):
    if len(re.findall(f"https:\/\/static.wikia.nocookie.net\/(.*)\/images\/[a-zA-Z0-9]\/[a-zA-Z0-9][a-zA-Z0-9]\/",url)):
        return 2 #Direct File URL
    elif len(re.findall(f"https:\/\/genshin-impact.fandom.com\/",url)):
        return 1 #Wiki File URL
    return 0 #File Case

def defineFile(file:str):
    file_type = file.split('.')[-1]
    file_name = file.replace(file_type,"")
    return file_name, file_type

def checkExist(file:str):
    if not os.path.isdir("./download/"):
        os.mkdir("./download/")
        return False
    return os.path.isfile(f"./download/{file}")

dl_list = []

if __name__ == '__main__':
    print("PondJa Genshin Impact Fandom Wiki Image Downloader")
    if len(dl_list):
        for f in dl_list:
            dl(f)
    while(1):
        inp = input("File Name: ")
        if ".txt" in inp and os.path.isfile(f"./{inp}"):
            rse = ""
            with open(inp, 'r', encoding='utf-8') as infile:
                for line in infile:
                    rse = line
            l = rse.replace("', '", "','").replace("\"", "'").split(",")
            for ll in l:
                dl(ll.replace(".ogg '", ".ogg").replace("'VO","VO").replace(".ogg'",".ogg"))
        else:
            dl(inp)