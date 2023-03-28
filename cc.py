import sys
import requests 
import json
from bs4 import BeautifulSoup
from pyfiglet import Figlet 
import colorama
import time
import asyncio
import os
from corex import bin

def detect_os():
    if "win" in sys.platform:
        return "windows"
    else:
        return "linux"


rd = colorama.Fore.RED
cv = colorama.Fore.WHITE
mag = colorama.Fore.MAGENTA
bl = colorama.Fore.BLUE
gn = colorama.Fore.GREEN
yl = colorama.Fore.YELLOW
cy = colorama.Fore.CYAN
gg = colorama.Fore.LIGHTCYAN_EX


def logo():
    figlet = Figlet(font="standard").renderText("Axid CC")
    return (gn + figlet)
print (logo())
print (bl + "[-] Powered by Axid")
print (gn + "[+] Made By Pomerd")
print (cy + "[=] Axid CC Tool Versiyonu : 0.1")

opr = input (mag + "\n[x] 1) Tek geçerli CC oluştur\n[x] 2) Çoklu geçerli CC oluştur (CC listesi oluşturur)\n[x] 3) CC Checker\n[x] 4) Çoklu Bin Numarası Oluştur \n\n[^] Bir fonksiyon gir :  ")

def genscard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    card = data['creditCard'][1]
    return (gn + "[-] Kart : %s\n[-] Kart Numarası : %s\n[-] Banka : %s\n[-] İsim : %s\n[-] Adres : %s\n[-] Ülke : %s\n[-] Tahmini Para Aralığı : %s\n[-] CVV : %s\n[-] M/Y : %s\n[-] Pin : %s\n============================\n[*] Discord Sunucusu : discord.gg/axid" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']) + cv)

def genmcard():
    cookies = {"csrftoken":"8b56rI96TwUH0X7dOT86JmPMBbUVYEpX3EI7ZKp3ZXHWnrRySD9ORyNaAaRXnW7i","_ga":"GA1.2.1579916434.1654760883","_gid":"GA1.2.1410860416.1654760883","_gads":"ID=d4f0fe2265535514-2243e178fad30069:T=1654760893:RT=1654760893:S=ALNI_MaIzJo5Kmg3rKoLXSuvDGnQkyW3uw","_gpi":"UID=0000087f297f7f43:T=1654760893:RT=1654760893:S=ALNI_MbnajBnRWmSHW7vrpR-U1w2uMwyVw",'FCNEC':'[["AKsRol_6etCde6kaPNd_o13SF2anvKLy0qaXvN6Kz0O_d9YbYS_KOfZ-j0xDjsEXL_4Otx5R38juHOOwfg0JShy5DHGmgAw2R6ZN4KZyI3qGimMjR0mQ0SEgj2ncvV4jQ32pssYst9ml2ptS_Ip2XyPbrLivgKXjIQ=="],null,[]]'}
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36","content-type":"application/x-www-form-urlencoded","x-csrftoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj","x-requested-with":"XMLHttpRequest"}
    payload = {"brand":"VISA","country":"UNITED STATES","bank":"121 FINANCIAL C.U.","cvv":"","date":"","year":"","range":"500 - 1000","amount":"10","dataformat":"TEXT","pin":"on","ctoken":"xr2Iy5sVk1nFVZaOfDTiLTU03sLe4oLYsUFJ67ISqsaUitU9jnU0T5So2rIgtGtj"}
    sitex = "https://www.vccgenerator.org/fetchdata/generate-home-credit-card/"
    rs = requests.post(sitex , headers=headers , cookies=cookies,data=payload)
    data = json.loads(rs.text)
    open("axid.txt","w").write("")
    for i in range(1,10):
        card = data['creditCard'][i]
        f = open("axid.txt","a")
        f.write("ange : %s\n[-] CVV : %s\n[-] Kart :[-] Marka : %s\n[-] Kart Numarası : %s\n[-] Banka : %s\n[-] İsim : %s\n[-] Adres : %s\n[-] Ülke : %s\n[-] Tahmini Para %s\n[-] Pin : %s\n===================================\n" % (card['IssuingNetwork'] , card['CardNumber'] , card['Bank'] , card['Name'] , card['Address'] , card['Country'] , card['MoneyRange'] , card['CVV'] , card['Expiry'] , card['Pin']))
    return (gn + "[$] Kartlar Oluşturuldu\n[+] axid.txt İsminde Kaydedildi" + cv)

def ccvalidator(number , type):
    site = "https://www.tools4noobs.com/"
    payload = {"action":"ajax_credit_card_validate","text":number,"cc":type}
    result = requests.post(site , data=payload)
    soup = BeautifulSoup(result.text ,"html.parser")
    return (bl + soup.text + cv)

if opr == "1":
    print (cy + "[&] İlk seçeneği seçtiniz ! \n\n")
    time.sleep(1)
    print (genscard())
elif opr == "2":
    print (yl + "[&] İkinci seçeneği seçtiniz ! \n\n")
    print (genmcard())
elif opr == "3":
    print (mag + "[&] Üçüncü seçeneği seçtiniz !! \n\n")
    number = input(yl + "[$] Lütfen kart numaranısı giriniz : ")
    if detect_os() == "windows":
        popen = os.popen("node corex\\val.js " + number).read()
        print (bl + popen + cv)
    else:
        popen = os.popen("node corex/val.js " + number).read()
        print (bl + popen + cv)
elif opr == "4":
    print (bl + "[&] Dördüncü seçeneği seçtiniz !")
    time.sleep(0.3)
    number = input(gn + "[-] Lütfen Bin Numarası Giriniz -  > ")
    round = input(cy + "[+] Bir Miktar Giriniz : (10) - > ")
    print (rd)
    bin.bin_generator(number , round)
    print ("Kaydedildi bin_oluşturuldu.txt !")
    print (mag + "[$] Discord Sunucusu : discord.gg/axid" + cv)
