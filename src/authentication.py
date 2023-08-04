from programInterface import *

class Credentials:
    def __init__(self, user, password):
        self.user = user
        self.password = password


def main():
    cred_list = []
    while(True):
        print("Hello, please choose an option")
        print("1. Create New Account")
        print("2. Login")
        print("3. Exit")
        choice = int(input())
        if choice == 1:
            print("Enter your username")
            user = input()
            print("Enter your password")
            password = input()
            creds = Credentials(user, password)
            cred_list.append(creds)
            continue
        elif choice == 2:
            print("Username: ")
            user = input()
            print("Password: ")
            password = input()
            flag = 0
            for c in cred_list:
                if c.user == user and c.password == password:
                    print ("Valid credentials, you are logged in.")
                    flag = 1
                    printMenu()
                    break
            if flag == 0:
                print("Invalid credentials")
        elif choice == 3:
            quit()


if __name__ == "__main__":
    main()