from colorama import Fore, Style
from time import sleep
from os import system
from requests import get
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
r = get("https://raw.githubusercontent.com/Pomerd/cc/main/cc.py").text
with open("cc.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print(Fore.RED + "Güncelleme yapılıyor...")
    with open("cc.py", "w", encoding="utf-8") as f:
        f.write(r)
from cc import GuncelKod
guncelleme = []
for attribute in dir(Guncelkod):
    attribute_value = getattr(GuncelKod, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            guncelleme.append(attribute)    
    system("cls||clear")

