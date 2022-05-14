
# Place Wiki in wikitext var, this py will remove all except Voice Over file.

wikitext = """
{{CharacterTabs}}
{{LanguageTabs}}
{{Stub|Romanization, Translation.}}
__TOC__
== Story ==
{{VO
|character               = Yae Miko
|vo_01_01_subtitle       = Hello
|vo_01_01_file           = VO_{language}{character} Hello.ogg
""".split('\n')

character = ""
language = ""

finder = []

for i in wikitext:
    if "|character" in i:
        if (i.find("= ")):
            if not len(character):
                character = i[i.find("= ")+2:]
                if "{{ROOTPAGENAME}}" in character:
                    character = ""
    elif "|name" in i and not len(character):
        if (i.find("= ")):
            character = i[i.find("= ")+2:]
    elif "|language" in i:
        if (i.find("= ")):
            find = i[i.find("= ")+2:]
            if not len(language) and find != "en":
                language = i[i.find("= ")+2:].upper() + " "
    elif "= VO" in i:
        find = i[i.find("= VO")+2:]
        if ".ogg" in find:
            finder.append(find.replace("{character}", character).replace("{language}", language).replace("_"," "))
    elif "{{A|VO" in i:
        find = i[i.find("{{A|VO")+4:].replace("}}","").replace("<!--","")
        if ".ogg" in find:
            finder.append(find.replace("{character}", character).replace("{language}", language).replace("_"," "))

f = list(set(finder))
f.sort()
print(f)