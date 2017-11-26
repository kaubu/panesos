# handler.py
# Handles commands

# Imports
import gvars
from os import system
from bcrypt import hashpw, checkpw, gensalt
from hashlib import sha256
from base64 import b64encode
from getpass import getpass
from pickle import load, dump
from sys import exit
from datetime import datetime

# Variables
pub_c = gvars.public_commands
prv_c = gvars.private_commands

## Functions
# General
def cache_credentials():
	try:
		with open(gvars.user_database, "rb") as file:
			return load(file)
	
	except FileNotFoundError:
		return {}

def hash_password(password):
	return hashpw(b64encode(sha256(password).digest()), gensalt())

def check_user(username):
	users = cache_credentials()

	if username in users:
		return True

	else:
		return False

def silent_update(): 
	system(gvars.silent_update)
	exit()

# PUBLIC
def pub_help():
	global pub_c
	for command in pub_c: print(command)

def pub_create():
	new_username = input("Username: ")
	new_display_name = input("Display Name: ")
	new_password = hash_password(getpass("Password: ").encode("utf-8"))

	users = cache_credentials()
	
	if check_user(new_username):
		print(gvars.username_taken_msg)

	else:
		dt = datetime.now()
		new_make_date = "{}-{}-{} - {}:{}:{}h".format(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)
		new_change_date = "{}-{}-{} - {}:{}:{}h".format(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)

		print("Creating the user...")
		users[new_username] = [new_display_name, new_password, new_make_date, new_change_date] # Second date it password reset date

		with open(gvars.user_database, "wb") as file:
			dump(users, file)

		print(gvars.new_user_msg)

		silent_update()

def pub_login():
	users = cache_credentials()

	try_username = input("Username: ")
	try_password = b64encode(sha256(getpass("Password: ").encode("utf-8")).digest())

	if check_user(try_username):
		hashed_password = users.get(try_username)[1]

		if checkpw(try_password, hashed_password): print("Authenticated with {}".format(users.get(try_username)[0]))
		else: print(gvars.auth_fail_msg)

	else:
		print(gvars.auth_fail_msg)

	silent_update()

def pub_chpwd():
	users = cache_credentials()

	try_username = input("Username: ")
	try_password = b64encode(sha256(getpass("Existing Password: ").encode("utf-8")).digest())
	new_password = hash_password(getpass("New Password: ").encode("utf-8"))

	dt = datetime.now()
	new_change_date = "{}-{}-{} - {}:{}:{}h".format(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)

	if check_user(try_username):
		hashed_password = users.get(try_username)[1]

		if checkpw(try_password, hashed_password):
			if not checkpw(try_password, new_password):
				old_user = users[try_username]
				users[try_username] = [old_user[0], new_password, old_user[2], new_change_date]

				with open(gvars.user_database, "wb") as file:
					dump(users, file)

				print(gvars.password_changed)

			else: print(gvars.same_pass_error)

		else: print(gvars.auth_fail_msg)

	else:
		print(gvars.auth_fail_msg)

	silent_update()

def pub_rmusr():
	users = cache_credentials()

	try_username = input("Username: ")
	try_password = b64encode(sha256(getpass("Password: ").encode("utf-8")).digest())

	if check_user(try_username):
		hashed_password = users.get(try_username)[1]

		if checkpw(try_password, hashed_password):
			users.pop(try_username, None)

			with open(gvars.user_database, "wb") as file:
				dump(users, file)

			print(gvars.account_removed)

		else: print(gvars.auth_fail_msg)

	else:
		print(gvars.auth_fail_msg)

	silent_update()

def pub_clear():
	system("cls")

def pub_reset():
	pub_clear()
	print(gvars.welcome_msg)

def pub_exit():
	exit()

# PRIVATE
def prv_prv():
	global prv_c
	for command in prv_c: print(command)

def prv_fupdate():
	system(gvars.force_update)
	exit()

def prv_users():
	users = cache_credentials()

	print("Format:\n[Username - Display Name]")
	for k, v in users.items():
		print("{} - {}".format(k, v[0]))

def prv_info():
	users = cache_credentials()

	try_username = input("Username: ")

	if check_user(try_username):
		user_info = users[try_username]
		print("User Info for {}\nUsername (Logon Name): {}\nDisplay Name: {}\nAccount Made: {}\nPassword Last Set: {}".format(try_username, try_username, user_info[0], user_info[2], user_info[3]))

	else: print(gvars.username_error)

def prv_retrievehash():
	users = cache_credentials()

	try_username = input("Username: ")

	if check_user(try_username):
		user_info = users[try_username]
		print(user_info[1])

	else: print(gvars.username_error)

# Classes
class handler:
	def __init__(self):
		self.new = True

	def process(self, command):
		if command in self.pub_c:
			exec("pub_{}()".format(command))

		elif command in self.prv_c:
			exec("prv_{}()".format(command))

	def refresh(self):
		global pub_c
		global prv_c

		self.pub_c = gvars.public_commands
		self.prv_c = gvars.private_commands