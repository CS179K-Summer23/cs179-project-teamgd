from MainMenu import *
from loginEncryption import *
import logging

class Credentials:
    def __init__(self, user, password):
        self.user = user
        self.password = password


def printLoginMenu():
    menu_options = ["Hello, please choose an option", "1. Create New Account", "2. Login", "3. Change Password", "4. Delete User", "5. Exit"]
    while(True):
        for option in menu_options:
            print(option)
        print("Select an option: ", end = "")
        choice = input()
        if choice == "1": #Create New Account
            encryptCheck()
            loginDecrypt()
            usernameQuery()
            loginEncrypt()
            print("New login successfully created!")
        elif choice == "2": #Login
            print("Username: ", end = "")
            user = input()
            print("Password: ", end = "")
            password = input()
            encryptCheck()
            loginDecrypt()		
            try:
                 if(login(user, password)):
                      print("Login Successful!")
                      loginEncrypt()
                      printMenu()
                 else:
                      print("Username/Password Invalid!")
                      loginEncrypt()
            except Exception as Argument:
                 logging.exception("Unknown error has occurred!")
                 encryptCheck()
        elif choice == "3": #Change Password
            print("This feature hasn't been implemented yet...")
        elif choice == "4": #Delete User
            print("This feature hasn't been implemented yet...")
        elif choice == "5": #Exit
            quit()


if __name__ == "__main__":
    printLoginMenu()