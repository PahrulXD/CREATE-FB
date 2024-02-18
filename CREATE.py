import os, sys, requests, fbthon, random, json
from fbthon import CreateAccount
from fake_email import Email
mail = Email().Mail()
x = (mail["mail"])

def masuk():
	os.system ("clear")
	firstname = input ("\033[1;97m- nama depan : \033[1;92m")
	lastname = input ("\033[1;97m- nama belakang : \033[1;92m")
	email = (x)
	ultah = "01/01/2000"
	gender = input ("\033[1;97m- jenis kelamin ( Male/Female ) : \033[1;92m")
	password = input ("\033[1;97m- password : \033[1;92m")
	print("")
	new_account = CreateAccount(firstname = firstname, lastname = lastname, email = email, gender = gender, date_of_birth = ultah, password = password)
	
	while True:
		mess=Email(mail["session"]).inbox()
		if mess:
			c =mess['topic'].split(' ')[0].replace("FB-","")
			break
		
	kode = (c)
	konfir = new_account.confirm_account(kode)
	 
	if konfir:
		print ("\033[1;97m- STATUS : \033[1;92mBERHASIL\033[1;97m")
		print ("\033[1;97m- nama akun : %s %s" % (firstname,lastname))
		print ("\033[1;97m- ID : %s" % (new_account.get_cookie_dict()['c_user']))
		print ("\033[1;97m- email : %s" % (email))
		print ("\033[1;97m- jenis kelamin : %s" % (gender))
		print ("\033[1;97m- TTL : %s" % (ultah))
		print ("\033[1;97m- password : %s" % (password))
		ip = requests.get("https://api.ipify.org").text
		print ("\033[1;97m- IP :\033[1;92m",ip)
		print ("\033[1;97m- cookie akun : %s" % (new_account.get_cookie_str()))
		print ("\033[1;97m- token akun : %s" % (new_account.get_token()))
		exit()
	else:
		print("\033[1;97m- STATUS : \0331;91mGAGAL !")
		exit()
		
		
masuk()