
def printMenu():
    print("----------")
    print("Main Menu:")
    print("----------")
    print("1. open document")
    print("2. upload document")
    print("3. delete document")
    print("4. sort documents\n")
    inp = input("Please input the number corresponding to the desired function to be executed:\n")
    if inp == "1":
        print("\n")
        printQueryMenu()
        inp2 = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp2 == "1":
            print("\n")
            printSubMenu()
            userInput()
        elif inp2 == "2":
            print("\n")
            printSubMenu()
            userInput()
        elif inp2 == "3":
            print("\n")
            printSubMenu()
            userInput()
        else:
            print("Unknown input. Returning to main menu.\n")
            printMenu()
    elif inp == "2":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "3":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "4":
        print("\n")
        temporaryFeatureMenu()
    else:
        print("Unknown input. Please try again.\n")
        printMenu()

def printQueryMenu():
    print("--------------")
    print("Query Options:")
    print("--------------")
    print("1. query based on document name")
    print("2. query based on document character count")
    print("3. query based on document length\n")

def printSubMenu():
    print("---------")
    print("Sub Menu:")
    print("---------")
    print("1. edit document")
    print("2. convert document")
    print("3. pin document")
    print("4. retrieve document statistics\n")

def userInput():
    inp = input("Please input the number corresponding to the desired function to be executed:\n")
    if inp == "1":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "2":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "3":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "4":
        print("\n")
        temporaryFeatureMenu()
    else:
        print("Unknown input. Please try again.\n")
        printSubMenu()
        userInput()
        
def temporaryFeatureMenu():
    print("------------------------")
    print("Respective Feature Menu:")
    print("------------------------")
    print("1. return to main menu\n")
    inp = input("Please input the number corresponding to the desired function to be executed:\n")
    if inp == "1":
        print("\n")
        printMenu()
    else:
        print("Unknown input. Please try again.\n")
        temporaryFeatureMenu()