from MainMenu import *
from loginEncryption import *

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
            loginDecrypt()
            usernameQuery()
            loginEncrypt()
        elif choice == "2": #Login
            print("Username: ", end = "")
            user = input()
            print("Password: ", end = "")
            password = input()
            loginDecrypt()
            try:
                 if(login(user, password)):
                      print("Login Successful!")
                      loginEncrypt()
                      printMenu()
                 else:
                      print("Username/Password Invalid!")
                      loginEncrypt()
            except:
                 print("Unknown error has occurred!")
                 loginEncrypt()
        elif choice == "3": #Change Password
            print("This feature hasn't been implemented yet...")
        elif choice == "4": #Delete User
            print("This feature hasn't been implemented yet...")
        elif choice == "5": #Exit
            quit()


if __name__ == "__main__":
    printLoginMenu()