from MainMenu import *
from loginEncryption import *
from loginCredentials import *
import logging

class Credentials:
    def __init__(self, user, password):
        self.user = user
        self.password = password


def printLoginMenu():
    menu_options = ["\n-------------------------------", "Hello, please choose an option:", "-------------------------------", "1. Create New Account", "2. Login", "3. Change Credentials", "4. Forgot Password", "5. Exit"]
    while(True):
        for option in menu_options:
            print(option)
        print("\nSelect an option: ", end = "")
        choice = input()
        if choice == "1": #Create New Account
            encryptCheck()
            loginDecrypt("login")
            usernameQuery()
            loginEncrypt("login")
            print("New login successfully created!")
        elif choice == "2": #Login
            print("Username: ", end = "")
            user = input()
            print("Password: ", end = "")
            password = input()
            encryptCheck()
            loginDecrypt("login")		
            try:
                 if(login(user, password)):
                      print("Login Successful!")
                      loginEncrypt("login")
                      printMenu()
                 else:
                      print("Username/Password Invalid!")
                      loginEncrypt("login")
            except Exception as Argument:
                 logging.exception("Unknown error has occurred!")
                 encryptCheck()
        elif choice == "3": #Change Credentials
            printCredentialMenu()
        elif choice == "4": #Forgot Password
            pass
        elif choice == "5": #Exit
            quit()

def printCredentialMenu():
    menu_options = ["\n---------------------------------------------------", "Please choose a credential that you want to change:", "---------------------------------------------------", "1. Change Username", "2. Change Password", "3. Change Security Questions", "4. Delete User", "5. Go Back"]
    while(True):
        for option in menu_options:
            print(option)
        print("\nSelect an option: ", end = "")
        choice = input()
        if choice == "1": #Change username
            encryptCheck()
            loginDecrypt("login")
            print("Enter username you want to change > ", end = "")
            username = input()
            if not usernameCheck(username):
                print("Enter password to authenticate > ", end = "")
                password = input()
                if login(username, password):
                    print("Enter new username > ", end = "")
                    newUsername = input()
                    changeUsername(newUsername)
                    print("Username succesfully changed!")
                else:
                    print("Password is incorrect!")
            else:
                print("User does not exist!")
                loginEncrypt("login")
        elif choice == "2": #Change password
            encryptCheck()
            loginDecrypt("login")
            print("Enter username > ", end = "")
            username = input()
            if not usernameCheck(username):
                print("Enter old password > ", end = "")
                oldPassword = input()
                if login(username, oldPassword):
                    print("Enter new password > ", end = "")
                    newPassword = input()
                    changePassword(username, newPassword)
                    print("Password successfully changed!")
                else:
                    print("Password is incorrect!")
            else:
                print("User does not exist!")
            loginEncrypt("login")
        elif choice == "3": #Change Security Questions
            pass
        elif choice == "4": #Delete User
            print("Enter the admin password to continue > ", end = "")
            adminPassword = input()
            if not adminCheck(adminPassword):
                print("Admin password is invalid! You may not delete a user.")
            else:
                encryptCheck()
                loginDecrypt("login")
                print("Enter the username of the user you want to delete > ", end = "")
                username = input()
                if not usernameCheck(username):
                    print("Enter user's password to confirm deletion > ", end = "")
                    password = input()
                    if login(username, password):
                        deleteUser(username)
                        print("User successfully deleted!")
                    else:
                        print("Password is incorrect!")
                else:
                    print("User does not exist!")
                loginEncrypt("login")
        elif choice == "5": #Go Back
             return

if __name__ == "__main__":
    printLoginMenu()
