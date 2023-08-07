from MainMenu import *
from loginEncryption import *

class Credentials:
    def __init__(self, user, password):
        self.user = user
        self.password = password


def printLoginMenu():
    cred_list = []
    while(True):
        print("Hello, please choose an option")
        print("1. Create New Account")
        print("2. Login")
        print("3. Exit")
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
        elif choice == "3": #Exit
            quit()


if __name__ == "__main__":
    printLoginMenu()