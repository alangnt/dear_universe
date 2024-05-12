from openpyxl import load_workbook
import pandas as pd
from time import sleep

filename = "Dear_Universe/dear_universe.xlsx"
dearuni_db = load_workbook(filename)
users_db = pd.read_excel(filename, sheet_name="Users", header=0)

def app_logo():
    print("~~~~~~~~~~~~~")
    print("Dear Universe")
    print("~~~~~~~~~~~~~\n")
    app_menu()

def app_menu():
    print("1. Create account")
    print("2. Sign in")
    print("3. Quit\n")
    menu_choice()

def menu_choice():
    while True:
        try:
            i = input("What is your choice ? > ")
            if i in ["1", "2", "3"]:
                if i in "3":
                    quit_program()
                elif i in "2":
                    user_account_signin()
                    break
                elif i in "1":
                    user_account_creation()
                    break
            else:
                raise AssertionError
            
        except AssertionError:
            print("An error has occured.\n")

def quit_program():
    quit()

def user_account_signin():
    global user_email
    user_email = input("What is your email adress ? > ")
    global check_email
    check_email = users_db.loc[users_db["User_Email"] == user_email].get("User_Email").to_string(index=False)
    user_password_try()

def user_password_try(attempts=3):
    while True:
        if user_email == check_email:
            while True:
                user_password = input("What is your password ? > ")
                check_password = users_db.loc[(users_db["User_Email"] == user_email) & (users_db["User_Password"] == user_password)].get("User_Password").to_string(index=False)
                if user_password == check_password:
                    user_name = users_db.loc[(users_db["User_Email"] == user_email) & (users_db["User_Password"] == user_password)].get("User_ID").to_string(index=False)
                    print(f"\nWelcome {user_name} ! You've successfully signed in !")
                    break
                else:
                    attempts += -1
                    print(f"\nSorry, the email and/or password don't match out database. Attempts: {attempts}\n")
                    if attempts == 0:
                        print("You tried 3 wrong passwords. The application is going to close in three seconds.") ; sleep(3)
                        quit()
        else:
            print("Sorry, we can't find your email in our database. Please try again.\n")
            user_account_signin()

def user_account_creation():
    print("Welcome ! Here's a few questions so we can get started :\n")

    user_id = input("Choose an id > ")
    user_firstname = input("What is your first name ? > ")
    user_lastname = input("What is your last name ? > ")
    user_email = input("What is your email adress ? > ")
    user_password = input("Choose a password > ")

    add = dearuni_db.active
    add_user = [[user_id, user_firstname, user_lastname, user_email, user_password]]

    for row in add_user:
        add.append(row)

    dearuni_db.save(filename)
    
app_logo()