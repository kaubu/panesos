# panes.py
# The "operating system" itself

# Imports
import gvars
import handler
from sys import argv

# Variables
new_launch = True

# Functions
def main():
	global new_launch

	try:
		if argv[1] == "update":
			print(gvars.update_msg)
			new_launch = False

		elif argv[1] == "silent-update":
			new_launch = False

		else:
			print("[INFO] Unknown argument/s detected:\n{}".format(argv[1:]))

	except (NameError, IndexError):
		pass

	chand = handler.handler()
	chand.refresh()

	if new_launch: 
		chand.process("clear")
		print(gvars.welcome_msg)

	while True:
		chand.refresh()

		try:
			chand.process(input("> "))

		except Exception as error:
			if gvars.allow_errors: print(error)

# Main
if __name__ == "__main__":
	main()