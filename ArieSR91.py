import os, sys, time

def clear():
    os.system("clear")
def ulang():
    os.system("python ArieSR91.py")
clear()

print ('''
__________________________      _______      __________________________
        ACCESS DENIED     \    / LOGIN \    /   ENTER THE PASSWORD
    \__________________/       \_______/       \__________________/
----------------------------√√^√^√^√^√\✓√\^----------------------------
''')
username = input("                      [@] Username: ")
password = input("                      [*] Password: ")
if password == "******":
    print("")
else:
    print("\n                        Password Wrong")
    lagi = input("                        try again [Y/n]: ")
    if lagi == "y":
         ulang()
    else:
         sys.exit()
clear()

def sukses():

    print ("__________________________     _________     __________________________")
    print ("        LOGIN SUCCESS     \   / SUCCESS \   /       @"+username)
    print ("    \__________________/      \_________/      \__________________/")
    print (" ")
    print ("------------------------------[ WELCOME ]------------------------------")

    time.sleep(0.1)

    print ("_________________________                     _________________________")
    print ("      \  ACCESS GRANTED  \   _____________   /     INDONESIA    /      ")
    print ("______/_____________________/ Hello World \_____________________\______")
    print ("______________________/     \_____________/     \______________________")
    print ("______________________\    ArieSR91 tools V1    /______________________")
    print ("|---------------------------------------------------------------------|")
    print ("|          _________________________________________________          |")
    print ("|         /   |             \ List script /             |   \         |")
    print ("|        /    |                                         |    \        |")
    print ("|       /     |       [1] Install user91 tools          |     \       |")
    print ("|      /      |       [2] Spam_SCW-V1                   |      \      |")
    print ("|     /____   |       [3] Spam_SCW-V2                   |   ____\     |")
    print ("|     |    |  |       [4] Spam_SCW-V3                   |  |    |     |")
    print ("|  |—————| |  |       [5] Spam_SCW-V4                   |  | |—————|  |")
    print ("|  |—————| |  |       [6] Spam_WA                       |  | |—————|  |")
    print ("|     |____|  |       [7] Trojans Attack                |  |____|     |")
    print ("|     \       |       [8] DDoS Hammer Attack            |       /     |")
    print ("|      \      |       [9] Bug Hunter                    |      /      |")
    print ("|       \     |      [10] Deface Website                |     /       |")
    print ("|        \    |      [00] Exit                          |    /        |")
    print ("|         \___|_________________________________________|___/         |")
    print ("|                                                                     |")
    print ("|---------------------------------------------------------------------|")
    print ("|                     __________________________                      |")
    pilih = input("|____________________/   Masukkan pilihan: ")
    if pilih == "1":
       os.system("pkg update && pkg upgrade && pkg install python && pkg install python2 && pkg install wget && pkg install curl && pkg install git && pkg install ruby && pip install lolcat && pkg install php && pkg install neofetch && pkg install nano && pkg install perl && pkg install nodejs && pkg install micro && pkg install joe && pkg install vim && pkg install jupp && pkg install zile && pkg install figlet && pkg install toilet && pkg install fish && pkg install cowsay && gem install ruby && pip install bs4 && python -m pip install requests && pip install requests && pip install mechanize && pip2 install --upgrade pip && pip2 install mechanize && pip2 install requests && pip2 install lolcat")
    if pilih == "2":
       os.system("python user91-spamV1.py")
    if pilih == "3":
       os.system("python user91-spamV2.py")
    if pilih == "4":
       os.system("python2 user91-spamV3.py")
    if pilih == "5":
       os.system("python user91-spamV4.py")
    if pilih == "6":
       os.system("python2 user91-spamWA.py")
    if pilih == "7":
       os.system("python2 trojans.py")
    if pilih == "8":
       os.system("python hammer.py")
    if pilih == "9":
       os.system("php rhawk.php")
    if pilih == "10":
       os.system("python deface.py")
    if pilih == "00":
       sys.exit()
sukses()
