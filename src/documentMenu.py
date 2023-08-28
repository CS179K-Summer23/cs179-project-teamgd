import json
import csv
from importjsonDoc import *
from tkinter import *
from DocumentStat import *

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
documentpath = parentpath + "/documents/"

def printDocumentMenu(filepath, choice, filename=""):
    # with open(documentpath + filepath) as json_file:
    #     jsondict = json.load(json_file)
    
    # print(jsondict)
    # print(jsondict[1]['Age'])
    # print(len(jsondict))
    # list_of_the_keys = list(jsondict.keys())
    while(True):
        print("--------------")
        print("Document Menu:" + filename)
        print("--------------")
        print("1. edit document")
        print("2. search document")
        print("3. retrieve document statistics")
        print("4. download document")
        print ("5. get value")
        print("6. return to main menu\n")
        # print(filepath)
        inp = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp == "1":
            print("\n")
            editDocument(filepath)
        elif inp == "2":
            print("\n")
            searchDocument(filepath)
        elif inp == "3":
            print("\n")
            getDocumentStatistics(filepath)
        elif inp == "4":
            print("\n")
            downloadDocument(documentpath + filepath, filepath, choice)
            break
        elif inp == "5":
            print("\n")
            getValue(filepath)
        elif inp == "6":
            print("\n")
            break
        else:
            print("Unknown input. Please try again.\n")


def editDocument(filepath):
    #set up window
    texteditor = Tk()
    texteditor.geometry("400x400")
    texteditor.title("Text Editor")
    scrollbar = Scrollbar(texteditor)
    scrollbar.pack(side=RIGHT, fill=Y)
    statusbar = Label(texteditor, text = 'Ready', anchor=E)
    statusbar.pack(fill=X, side=BOTTOM, ipady=5)
    
    text = Text(texteditor, yscrollcommand=scrollbar.set)
    text.pack(fill=BOTH)
    scrollbar.config(command=text.yview)
    
    #set up file
    def open_file():
        textfile = open(documentpath + filepath, 'r')
        content = textfile.read()
        text.insert(END, content)
        textfile.close()
    #save file
    def save_file():
        textfile = open(documentpath + "temp.json", 'w')
        textfile.write(text.get(1.0, END))
        textfile.close()
        if(validateJSON(documentpath + "temp.json")):
            textfile = open(documentpath + filepath, 'w')
            textfile.write(text.get(1.0, END))
            textfile.close()
            statusbar.config(text=f'Saved')
        else:
            statusbar.config(text=f'File is not correct Json Format')
    #set up buttons
    mymenu = Menu(texteditor)
    texteditor.config(menu=mymenu)
    filemenu = Menu(mymenu, tearoff=False)
    mymenu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Load File", command=open_file)
    filemenu.add_command(label="Save", command=save_file)
    
    open_file()
    texteditor.mainloop()

def searchDocument(filepath):
    print("\nPlease enter search word:")
    choice = str(input())
    tempcount = 0
    with open(documentpath + filepath, 'r') as findword:
        for linenum, line in enumerate(findword):
            if choice in line:
                print(choice, "found on line", linenum+1)
                tempcount += 1
    if tempcount == 0:
        print(choice, " not found in file!")
    
def getDocumentStatistics(filepath):
    populateDataStat(documentpath + filepath)

def getValue(filepath):
    key = input("Enter a key: ")
    resultlist = []
    with open(documentpath + filepath, 'r') as json_file:
        data = json.load(json_file)
        getResults(data, resultlist, key)
    print(resultlist)

def getResults(data, resultlist, key):
    if type(data) is dict and key in data:
            resultlist.append(data.get(key))
    for item in data:
        if type(item) is (dict or list):
            getResults(item, resultlist, key)
        else:
            return