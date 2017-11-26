# launcher.py
# The Launcher for PanesOS

# Imports
from os import system
from sys import exit

# Main
if __name__ == '__main__':
	try:
		system("cd system && panes.py")
	except KeyboardInterrupt:
		print("\nThis program has been terminated. Goodbye!")
	exit()