from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms

sms_hizmetleri = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if not attribute.startswith('__'):
            sms_hizmetleri.append(attribute)

while True:
    system("cls||clear")
    print(f"""{Fore.LIGHTRED_EX}

    ▀▀█▀▀ ▀█▀ ▀▀█▀▀ ░█▀▀█ ▒█▄░▒█ ▀█▀ ▒█▀▀█ 　 ▒█░▒█ ▀█▀ ▀▀█▀▀ 
    ░▒█░░ ▒█░ ░▒█░░ ▒█▄▄█ ▒█▒█▒█ ▒█░ ▒█░░░ 　 ▒█▀▀█ ▒█░ ░▒█░░ 
    ░▒█░░ ▄█▄ ░▒█░░ ▒█░▒█ ▒█░░▀█ ▄█▄ ▒█▄▄█ 　 ▒█░▒█ ▄█▄ ░▒█░░
    
    Hizmet Sayısı: {len(sms_hizmetleri)}           {Fore.LIGHTBLUE_EX}by {Style.BRIGHT}@manlydev\n  
    """)

    try:
        menu = input(f"{Fore.LIGHTCYAN_EX} 1 - SMS Bomber\n\n 2 - Çıkış Yap\n\n{Fore.LIGHTYELLOW_EX}Seçenek: ")
        if not menu:
            continue
        menu = int(menu)
    except ValueError:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}[-] Geçersiz giriş. Lütfen tekrar deneyin.")
        sleep(3)
        continue

    if menu == 1:
        system("cls||clear")
        print(f"{Fore.LIGHTYELLOW_EX}[?] Telefon numarasını '+90' olmadan girin (Çoklu numaralar için 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}", end="")
        tel_no = input()
        tel_list = []

        if not tel_no:
            system("cls||clear")
            print(f"{Fore.LIGHTYELLOW_EX}[?] Telefon numaralarını içeren dosyanın dizinini girin: {Fore.LIGHTGREEN_EX}", end="")
            directory = input()

            try:
                with open(directory, "r", encoding="utf-8") as f:
                    for line in f.read().strip().split("\n"):
                        if len(line) == 10:
                            tel_list.append(line)
            except FileNotFoundError:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}[-] Geçersiz dosya dizini. Lütfen tekrar deneyin.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_list.append(tel_no)
            except ValueError:
                system("cls||clear")
                print(f"{Fore.LIGHTRED_EX}[-] Geçersiz telefon numarası. Lütfen tekrar deneyin.")
                sleep(3)
                continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}[?] E-posta adresi (Bilmiyorsanız 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}", end="")
            email = input()
            if ("@" not in email or ".com" not in email) and email:
                raise ValueError
        except:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}[-] Geçersiz e-posta adresi. Lütfen tekrar deneyin.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}[?] Kaç SMS göndermek istediğinizi girin (Sonsuz için 'enter' tuşuna basın): {Fore.LIGHTGREEN_EX}", end="")
            times = input()
            if times:
                times = int(times)
            else:
                times = None
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}[-] Geçersiz giriş. Lütfen tekrar deneyin.")
            sleep(3)
            continue

        system("cls||clear")
        try:
            print(f"{Fore.LIGHTYELLOW_EX}[?] Her SMS arasındaki süreyi saniye cinsinden girin: {Fore.LIGHTGREEN_EX}", end="")
            interval = int(input())
        except ValueError:
            system("cls||clear")
            print(f"{Fore.LIGHTRED_EX}[-] Geçersiz giriş. Lütfen tekrar deneyin.")
            sleep(3)
            continue

        system("cls||clear")
        if not times:
            sms = SendSms(tel_no, email)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if not attribute.startswith('__'):
                            exec("sms."+attribute+"()")
                            sleep(interval)
        for number in tel_list:
            sms = SendSms(number, email)
            if isinstance(times, int):
                    while sms.adet < times:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if not attribute.startswith('__'):
                                    if sms.adet == times:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(interval)
        print(f"{Fore.LIGHTRED_EX}[?] Menüye dönmek için 'enter' tuşuna basın...")
        input()
    elif menu == 2:
        system("cls||clear")
        print(f"{Fore.LIGHTRED_EX}[?] Çıkılıyor...")
        break
