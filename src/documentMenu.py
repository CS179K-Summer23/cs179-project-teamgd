from importjsonDoc import *

def printDocumentMenu(filepath):
    while(True):
        print("---------")
        print("Document Menu:")
        print("---------")
        print("1. edit document")
        print("2. convert document")
        print("3. retrieve document statistics")
        print("4. return to main menu\n")
        inp = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp == "1":
            print("\n")
            editDocument()
        elif inp == "2":
            print("\n")
            convertDocument(filepath)
        elif inp == "3":
            print("\n")
            getDocumentStatistics()
        elif inp == "4":
            print("\n")
            break
        else:
            print("Unknown input. Please try again.\n")


def editDocument():
    print("X")

def convertDocument(filepath):
    print("1. Convert CSV to JSON")
    print("2. Convert JSON to CSV")

    inp = input("Please input the number corresponding to the desired function to be executed:\n")

    if(inp == '1'):
        convertToJson(filepath, filepath)
    print("X")

def getDocumentStatistics():
    print("X")
