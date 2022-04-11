text = """
;(Talk to Xiangling again)
:{{A|vo dialog eqzyj002 xiangling 01.ogg}} '''Xiangling:''' Hmm, everyone's here to eat, what should I cook? Lemme think... I've got some Fowl and some Fish... and Shrimp Meat, so I can do two snack dishes... yes, and a few stir-fries!
:{{A|vo dialog eqzyj002 xiangling 02.ogg}} '''Xiangling:''' Hee-hee, everyone's gonna love it.

;(Talk to Zhongli, มาดาม Ping, or Guoba again)
:{{A|vo dialog eqzyj002 zhongli 01.ogg}} '''Zhongli:''' The food at ภัตตาคาร Wanmin is excellent. I eat here often.
:{{A|vo dialog eqzyj002 madameping 01.ogg}} '''มาดาม Ping:''' You can say that again... Xiangling is a remarkable child, surely the culinary talent of the century.
:{{A|vo dialog eqzyj002 gooba 01.ogg}} '''Guoba:''' ♪~♪!
:{{A|vo dialog eqzyj002 zhongli 02.ogg}} '''Zhongli:''' Indeed. To have mastered the craft at her age lends credence to the old aphorism that heroes are made young.
{{Dialogue end}}
""".split('\n')
f = open("output.txt", "w", encoding="utf-8")

for i in text:
    if "{{A|" in i:
        start = i.find("{{A|")
        end = i.find(".ogg}}")
        f.write(f":{str(i[end+7:])}\n")
    else:
        f.write(f"{i}\n")
f.close()