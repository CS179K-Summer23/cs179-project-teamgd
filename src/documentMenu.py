import json
import csv
from importjsonDoc import *
from tkinter import *
from DocumentStat import *
import pandas as pd

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
documentpath = parentpath + "/documents/"

def printDocumentMenu(filepath, choice, filename=""):
    with open(filepath) as j:
            data = json.load(j)
            df = pd.json_normalize(data)
    column_names = list(df)
    while(True):
        print("--------------")
        print("Document Menu: " + filename)
        print("--------------")
        print(df)
        print("--------------\n")
        print("Options: ")
        print("1. Add row")
        print("2. Edit row")
        print("3. Search document")
        print("4. Get value")
        print("5. Document Statistics")
        print("6. Download document")
        print("7. Open Document in Text Editor")
        print("8. Save and Return\n")
        # print(filepath)
        inp = input("Please input the number corresponding to the desired function to be executed:\n")
        if inp == "1":
            tempdict = {}
            for x in range(len(column_names)):
                print("Enter a " + column_names[x] + ":")
                choice = str(input())
                tempdict[column_names[x]] = choice
            # print(tempdict)
            with open(parentpath + "/data/tempsave.json", "w") as f:
                f.write(json.dumps(tempdict, indent=4))
            with open(parentpath + "/data/tempsave.json") as f:
                data2 = json.load(f)
                df2 = pd.json_normalize(data2)
            df = pd.concat([df, df2], ignore_index=True)
            continue
           
        if inp == "2":
            numrows = len(df)
            while(True):
                print("Enter row #: ")
                rowchoice = int(input())
                if(rowchoice >= numrows):
                    print("Invalid input. Please try again")
                else:
                    break
            print("Choose which Column to Edit:")
            print(column_names)
            while(True):
                colchoice = input()
                if colchoice in column_names:
                    break
                else:
                    print("Invalid input. Please try again")
            print("Enter new " + colchoice + ": ")
            inputchoice = input()
            df.iloc[rowchoice, df.columns.get_loc(colchoice)] = inputchoice
        elif inp == "3":
            print("\n")
            searchDocument(filepath, df)
        elif inp == "5":
            print("\n")
            getDocumentStatistics(filepath)
        elif inp == "6":
            print("\n")
            downloadDocument(filepath, filename, choice)
            break
        elif inp == "4":
            print("\n")
            getValue(filepath)
        elif inp == "7":
            print("\n")
            editDocument(filepath)
        elif inp == "8":
            print("\n")
            break
        else:
            print("Unknown input. Please try again.\n")
    exportDictionary = df.to_dict(orient="records")
    with open(filepath, "w") as f:
        f.write(json.dumps(exportDictionary, indent=4))


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
        textfile = open(filepath, 'r')
        content = textfile.read()
        text.insert(END, content)
        textfile.close()
    #save file
    def save_file():
        textfile = open(documentpath + "temp.json", 'w')
        textfile.write(text.get(1.0, END))
        textfile.close()
        if(validateJSON(documentpath + "temp.json")):
            textfile = open(filepath, 'w')
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

def searchDocument(filepath, df):
    numrows = len(df)
    column_names = list(df)
    # tempcount = 0
    # with open(filepath, 'r') as findword:
    #     for linenum, line in enumerate(findword):
    #         if choice in line:
    #             print(choice, "found on line", linenum+1)
    #             tempcount += 1
    # if tempcount == 0:
    #     print(choice, " not found in file!")
    typeresult = df.dtypes

    print("Column to search in:")
    print(column_names)
    while(True):
        colchoice = input()
        if colchoice in column_names:
            break
        else:
            print("Invalid input. Please try again")
    print("\nPlease enter search word:")
    choice = input()
    # print(typeresult[colchoice])
    searchresult = df[df[colchoice].str.contains(choice)]
    print("--------------")
    print(searchresult)
    print("--------------\n\n")
    while(True):
        print("Press any key to continue.")
        tempchoice = input()
        break


    
def getDocumentStatistics(filepath):
    populateDataStat(filepath)
    print("Press any key to continue:")
    input()

def getValue(filepath):
    key = input("Enter a key: ")
    resultlist = []
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
        getResults(data, resultlist, key)
    print(resultlist)

def getResults(data, resultlist, key):
    if type(data) is dict:
        if key in data:
            resultlist.append(data.get(key))
        for item in data.keys():
            if type(data[item]) is dict or type(data[item]) is list:
                getResults(data[item], resultlist, key)