# gvars.py
# A place for global variables to be stored

# Commands
public_commands = ["help", "create", "login", "clear", "exit"]
private_commands = ["prv", "fupdate", "users"]

# Path
user_database = "./user.db"
public_panes_entry = "../launcher.py"
panes_entry = "panes.py"
force_update = "panes.py update"
silent_update = "panes.py silent-update" # Silent update is only permitted by inbuilt functions

# Messages
welcome_msg = "Welcome! Please log in or create an account to get started.\nTry 'help' if you need any."
update_msg = "Updated successfully."
auth_fail_msg = "Username or password is incorrect."
new_user_msg = "User created successfully."
username_taken_msg = "Username has already been taken. Try another."

# Miscellaneous
allow_errors = True