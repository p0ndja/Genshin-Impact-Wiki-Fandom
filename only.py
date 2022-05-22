import re
# Place Wiki in wikitext var, this py will remove all except Voice Over file.

wikitext = """
{| class="wikitable" 
|-
! width="75px" | Character 
! width="150px" | Preferences !! Voice-Overs
|-
| rowspan="3" | {{Card|Albedo}}
!Like
| {{A|VO ZH Albedo Spice Like 01.ogg}} {{Lang|mini=1|zh=味觉仿佛折射出了色彩…我想它是金色的。|zh_rm=<br /><i><small>Wèijué fǎngfú zhéshè chūle sècǎi... Wǒ xiǎng tā shì jīnsè de.</small></i>}}
|-
!Neutral
| {{A|VO ZH Albedo Spice Neutral 01.ogg}} {{Lang|mini=1|zh=你似乎很愿意花时间在做菜上，所以才能做出这样的味道。|zh_rm=<br /><i><small>Nǐ sìhū hěn yuànyì huā shíjiān zài zuòcài shàng, suóyǐ cáinéng zuòchū zhèyàng de wèidào.</small></i>}}
|-
!Dislike
| {{A|VO ZH Albedo Spice Dislike 01.ogg}} {{Lang|mini=1|zh=量有点大…要一起分享吗？|zh_rm=<br /><i><small>Liàng yóudiǎn dà... Yào yīqǐ fēnxiǎng ma?</small></i>}}
""".split('\n')

character = ""
language = ""

finder = []

for i in wikitext:
    target = re.findall("VO (.*).ogg", i)
    if len(target):
        finder.append(f"VO {target[0]}.ogg")
        print(target)
print(finder)