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
		new_make_date = "{} {} {} - {} {} {}".format(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)

		print("Creating the user...")
		users[new_username] = [new_display_name, new_password, new_make_date]

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

def pub_clear():
	system("cls")

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