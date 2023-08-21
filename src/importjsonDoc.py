import json
import csv
import os
import shutil
from database import *

db = Database()

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
documentpath = parentpath + "/documents/"

def convertToJson(csvPath, jsonPath):
    data = []
    
    split = os.path.splitext(jsonPath)

    fileExtension = split[1]

    if(fileExtension == '.csv'):
        jsonPath = jsonPath.replace(".csv", ".json")
    else:
        print("Not CSV file")
        return
    
    with open(csvPath,"r") as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            # Currently uses Arbitrary key 'index'
            data.append(rows)
            
    with open(jsonPath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    # print("Success")
    
def convertToCsv(jsonPath):
    length = len(jsonPath)
    check = jsonPath[length - 5:]
        
    if check == ".json":
        pathElements = jsonPath.split("/")
        numOfElements = len(pathElements)
        fileToOpen = pathElements[numOfElements - 1]
        with open(documentpath + fileToOpen) as json_file:
            jsonData = json.load(json_file)
    
        inputSplit = fileToOpen.split(".")
        fileName = inputSplit[0] + ".csv"
        os.chdir("../documents")
        csvFile = open(fileName, "w")
        csvWriter = csv.writer(csvFile)
        
        flag = 0
        for data in jsonData:
            if flag == 0:
                header = data.keys()
                csvWriter.writerow(header)
                flag += 1
            
            csvWriter.writerow(data.values())
        
        csvFile.close()
        #flag = db.addFile(fileName)
        #if flag == 0:
        print("Success!\n")
        #elif flag == 1:
        #    print("Conversion unsuccessful. Please try again.")
        #    removalPath = os.path.join(os.getcwd(), fileName)
        #    os.remove(removalPath)
        os.chdir("../src")
        return fileName
    else:
        print("Unable to read input of json file, please try again.\n")

# Takes from local computer to the database
def uploadDocument(srcPath, destPath):
    split = os.path.splitext(srcPath)
    split1 = os.path.splitext(destPath)
    split1 = os.path.splitext(destPath)

    fileExtension = split[1]

    if(split1[1] == ""):
        destPath += '.json'

    if fileExtension == '.json':
        f = open(srcPath)
        data = json.load(f)
        with open(destPath, 'w') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
        f.close()
    else:
        print("Source File extension not JSON.")

def downloadDocument(jsonPath, filepath, choice):
    print("1. Download as JSON")
    print("2. Download as CSV\n")
    
    inp = input("Please input the number corresponding to the desired function to be executed:\n")
    
    if inp == "1":
        shutil.move(jsonPath, "../downloads/" + filepath)
        print("Downloaded to downloads folder!\n")
        db.deleteFile(filepath, choice, 1)
    elif inp == "2":
        fileToDownload = convertToCsv(jsonPath)
        shutil.move("../documents/" + fileToDownload, "../downloads/" + fileToDownload)
        print("Downloaded to downloads folder!\n")
    else:
        print("Unknown input, please try again.\n")
        downloadDocument(jsonPath, filepath)

# convertToJson("../documents/test.csv", "../documents/test.csv")
# uploadDocument("test2.json", "new2.json")
