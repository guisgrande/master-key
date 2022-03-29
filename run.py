
# NEW / MODIFY - Method to user insert a new personal password and to modify an old one.
def password_personal():
    print("Personal PW")

# NEW - Method to generate a new random password.
def password_random():
    print("Random PW")

# VERIFY - Method to user see the password.
def accounts_show():
    print("Show PW")

# VERIFY - Method to modify the password for a new one, will gona change (delete old - add the new).
def accounts_modify():
    print("Modify PW")

# VERIFY - Method to delete all information from a certain account selected by the user.
def accounts_delete():
    print("Delete data")

# MAIN MENU - Method to close the program - Option [Q]
def quit_program():
    print("Thanks! Closing the program.")

# MAIN MENU - Method to create a new account information and password - Option [N]
def new_password():
    print("NEW")

# MAIN MENU - Method to verify all accounts (see, modify or delete) - Option [V]
def verify_accounts():
    print("VERIFY")

def main():
    print("""
Chose one option:
[N] - New password
[V] - Verify accounts
[Q] - Quit the program
    """)
    option = input("Your selection: ")
    if option == 'N':
        new_password()
    elif option == "V":
        verify_accounts()
    elif option == "Q":
        quit_program()
    else:
        print("""
Wrong command! Should be one of the three options! 
[N] - New password
[V] - Verify accounts
[Q] - Quit the program
        """)
        print(option)

print("""
###########################################################
################# WELCOME TO MASTER KEY ###################
###########################################################
""")
main()


