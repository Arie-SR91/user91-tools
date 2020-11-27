#Hello World
#Script Deface by Syahri Ramadhan 91
#jangan disalahgunakan!
#pastikan anda sudah membuat script isi defacenya (index.html)
#letakkan di memori internal
#sebelum menjalankan, install curl terlebih dahulu.

import os, sys
import time

def ulang():
    os.system("python deface.py")
def clear():
    os.system("clear")
def mulai():
    os.system("bash deface.sh")

clear()

print ('''
_________________________      _______      ___________________________
       ACCESS DENIED     \    / LOGIN \    /    ENTER THE PASSWORD
    \_________________/       \_______/       \___________________/
---------------------------√√^√^√^√^√\✓√\^-----------------------------
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

print ("_________________________     _________     ___________________________")
print ("       LOGIN SUCCESS     \   / SUCCESS \   /       @"+username)
print ("    \_________________/      \_________/      \___________________/")
print (" ")
print ("-----------------------------[ WELCOME ]-------------------------------")

time.sleep(0.1)

print ("________________________                     __________________________")
print ("     \  ACCESS GRANTED  \   _____________   /     INDONESIA      /     ")
print ("_____/_____________________/ Hello World \_______________________\_____")
print ("_____________________/     \_____________/     \_______________________")
print ("_____________________\  Welcome to My Scripts  /_______________________")
print ("|---------------------------------------------------------------------|")
mulai()
print ("|---------------------------------------------------------------------|")


load = '#'
count = 0
for x in range(101):
    time.sleep(0.1)
    print(f'\rLOADING {x}% [{load}]', end='', flush=True)
    count += 1
    if count == 3:
        count = 0
        load += '#'
print ("\n")

print ("Website Defaced")
print (target)
again = input("Deface again [Y/n] ")
if again == "y":
   os.system("bash deface.sh")
else:
   sys.exit()
