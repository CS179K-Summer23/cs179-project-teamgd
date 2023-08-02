def printMenu():
    print("----------")
    print("Main Menu:")
    print("----------")
    print("1. query document")
    print("2. edit document")
    print("3. upload document")
    print("4. convert document")
    print("5. pin document")
    print("6. sort documents")
    print("7. retrieve document statistics\n")
    
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
    elif inp == "5":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "6":
        print("\n")
        temporaryFeatureMenu()
    elif inp == "7":
        print("\n")
        temporaryFeatureMenu()
    else:
        print("Unknown input. Please try again.\n")
        printMenu()
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
        userInput()
    else:
        print("Unknown input. Please try again.\n")
        temporaryFeatureMenu()
        
printMenu()
userInput()
