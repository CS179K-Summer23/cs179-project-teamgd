from MainMenu import *
from loginEncryption import *
from loginCredentials import *
import logging

def printLoginMenu():
    menu_options = ["\n-------------------------------", "Hello, please choose an option:", "-------------------------------", "1. Create New Account", "2. Login", "3. Change Credentials", "4. Forgot Password", "5. Exit"]
    while(True):
        encryptCheck()
        for option in menu_options:
            print(option)
        choice = input("\nSelect an option > ")
        if choice == "1": #Create New Account
            loginDecrypt("login")
            username = usernameQuery()
            loginEncrypt("login")
            print("New login successfully created!")
            answer = input("\nWould you like to create security questions for this account? (This is optional) > ")
            if answer.lower() == "y" or answer.lower() == "yes":
                securityEncryptCheck()
                loginDecrypt("security")
                questionList = getQuestionList()
                questionOne, newQuestionList = selectQuestion(questionList)
                questionTwo, newQuestionList = selectQuestion(newQuestionList)
                addSecurityQuestion(username, questionOne, questionTwo)
                print("Successfully added security questions!")
                loginEncrypt("security")
        elif choice == "2": #Login
            user = input("Username > ")
            password = input("Password > ")
            loginDecrypt("login")		
            try:
                 if(login(user, password)):
                      print("Login Successful!")
                      loginEncrypt("login")
                      printMenu(user)
                 else:
                      print("Username/Password Invalid!")
                      loginEncrypt("login")
            except Exception as Argument:
                 logging.exception("Unknown error has occurred!")
                 encryptCheck()
        elif choice == "3": #Change Credentials
            printCredentialMenu()
        elif choice == "4": #Forgot Password
            loginDecrypt("login")
            username = input("Enter a username for password retrieval > ")
            if not usernameCheck(username):
                securityEncryptCheck()
                loginDecrypt("security")
                if securityQuestionCheck(username):
                    if askQuestion(username):
                        print("\nThe password of \"" + username + "\" is: " + getPassword(username))
                    else:
                        print("Answer is incorrect!")
                else:
                    print("User does not have associated security questions! Cannot perform password retrieval!")
            else:
                print("User does not exist!")
            loginEncrypt("login")
        elif choice == "5": #Exit
            securityEncryptCheck()
            quit()

def printCredentialMenu():
    menu_options = ["\n---------------------------------------------------", "Please choose a credential that you want to change:", "---------------------------------------------------", "1. Change Username", "2. Change Password", "3. Change Security Questions", "4. Delete User", "5. Go Back"]
    while(True):
        encryptCheck()
        securityEncryptCheck()
        for option in menu_options:
            print(option)
        choice = input("\nSelect an option > ")
        if choice == "1": #Change username
            loginDecrypt("login")
            loginDecrypt("security")
            username = input("Enter username you want to change > ")
            if not usernameCheck(username):
                password = input("Enter password to authenticate > ")
                if login(username, password):
                    newUsername = input("Enter new username > ")
                    changeUsername(username, newUsername, "login.txt", 2)
                    changeUsername(username, newUsername, "security.txt", 3)
                    changeUsernameProfile(username, newUsername)
                    print("Username succesfully changed!")
                else:
                    print("Password is incorrect!")
            else:
                print("User does not exist!")
            loginEncrypt("login")
            loginEncrypt("security")
        elif choice == "2": #Change password
            loginDecrypt("login")
            username = input("Enter username > ")
            if not usernameCheck(username):
                oldPassword = input("Enter old password > ")
                if login(username, oldPassword):
                    newPassword = input("Enter new password > ")
                    changePassword(username, newPassword)
                    print("Password successfully changed!")
                else:
                    print("Password is incorrect!")
            else:
                print("User does not exist!")
            loginEncrypt("login")
        elif choice == "3": #Change Security Questions
            loginDecrypt("security")
            loginDecrypt("login")
            questionList = getQuestionList()
            print("Please enter login credentials to continue...")
            username = input("Enter a username > ")
            password = input("Enter a password > ")       
            if login(username, password):
                check = securityQuestionCheck(username)
                if check:
                    print("User aleady has security questions. Please answer security questions first before continuing...")
                    if askQuestion(username):
                        questionOne, newQuestionList = selectQuestion(questionList)
                        questionTwo, newQuestionList = selectQuestion(newQuestionList)
                        changeSecurityQuestion(username, questionOne, questionTwo)
                        print("Successfully changed security questions!")
                    else:
                        print("Answer is incorrect!")
                else:
                    print("User does not have security questions. Creating security questions for the first time...")
                    questionOne, newQuestionList = selectQuestion(questionList)
                    questionTwo, newQuestionList = selectQuestion(newQuestionList)
                    addSecurityQuestion(username, questionOne, questionTwo)
                    print("Successfully added security questions!")
            else:
                print("Login information is incorrect!")
            loginEncrypt("login")
            loginEncrypt("security")
        elif choice == "4": #Delete User
            adminPassword = input("Enter the admin password to continue > ")
            if not adminCheck(adminPassword):
                print("Admin password is invalid! You may not delete a user.")
            else:
                loginDecrypt("login")
                loginDecrypt("security")
                username = input("Enter the username of the user you want to delete > ")
                if not usernameCheck(username):
                    password = input("Enter user's password to confirm deletion > ")
                    if login(username, password):
                        deleteUser(username)
                        if securityQuestionCheck(username):
                            deleteSecurityQuestion(username)
                        print("User successfully deleted!")
                    else:
                        print("Password is incorrect!")
                else:
                    print("User does not exist!")
                loginEncrypt("login")
                loginEncrypt("security")
        elif choice == "5": #Go Back
             return

if __name__ == "__main__":
    printLoginMenu()
