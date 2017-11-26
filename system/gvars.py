# gvars.py
# A place for global variables to be stored

# Commands
public_commands = ["help", "create", "login", "chpwd", "rmusr", "reset", "clear", "exit"]
private_commands = ["prv", "fupdate", "users", "info", "retrievehash"]

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
password_changed = "Password changed successfully."
account_removed = "Account removed successfully."
username_error = "User does not exist."
same_pass_error = "Sorry, you can't change your password to the same password.\nIt's not really changing it is it?"

# Miscellaneous
allow_errors = False
version = "0.2"