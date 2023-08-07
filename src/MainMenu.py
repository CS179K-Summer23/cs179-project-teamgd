from database import *
from documentMenu import *
from importjsonDoc import *
from LoginMenu import *

db = Database()

def printMenu():
    while (True):
        print("----------")
        print("Main Menu:")
        print("----------")
        print("1. open document")
        print("2. upload document")
        print("3. delete document")
        print("4. sort documents")
        print("5. list documents")
        print("6. pin document")
        print("7. get database statistics")
        print("8. Logout\n")
        inp = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp == "1":
            print("\n")
            openDocument()
        elif inp == "2":
            print("\n")
            uploadDoc()
        elif inp == "3":
            print("\n")
            deleteDocument()
        elif inp == "4":
            print("\n")
            sortDocuments()
        elif inp == "5":
            print("\n")
            listDocuments()
        elif inp == "6":
            print("\n")
            pinDocument()
        elif inp == "7":
            print("\n")
            getDatabaseStats()
        elif inp == "8":
            return
        else:
            print("Unknown input. Please try again.\n")

def openDocument():
    db.printDocs()
    filepath = "../documents/" + db.getDoc()['name'] #docinfo is the json entry of the document in docinfo.json
    printDocumentMenu(filepath)

def uploadDoc():
    srcPath = input("Input file you want to upload: ")
    split = os.path.splitext(srcPath)
    
    if(os.path.isfile(srcPath) or split[1] == '.json' or split[1] == '.csv'):
    
        destPath = input("Input where you want to upload and file name: ")
        split1 = os.path.splitext(destPath)

        if(os.path.isfile(destPath) or os.path.isfile(destPath + '.json')):
            print("File already exists")
            return
        elif(os.path.isdir(destPath)):
            print("Directory exists, need filename")
            return
        elif(split1[1] != '.json'):
            print("Invalid file extension")
            return
        elif(not destPath):
            print("Invalid Input")
            return
    else:
        print("File does not exist or Invalid input")
        return
        

    
    # The uploadDocument function calls convertToJson function
    uploadDocument(srcPath, destPath) 

    print("upload document")

def deleteDocument():
    db.printDocs()
    #db.deleteFile()
    print("delete document")

def sortDocuments():
    db.printDocs()
    print("sort documents")

def listDocuments():
    db.printDocs()
    input("Press Enter to continue.")

def pinDocument():
    db.printDocs()

def getDatabaseStats():
    db.printDBMenu()

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