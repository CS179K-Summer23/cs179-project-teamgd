import json
import csv
import os
from database import *

db = Database()

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)

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
    print(jsonPath)
    length = len(jsonPath)
    check = jsonPath[length - 5:]
    print(check)
        
    if check == ".json":
        pathElements = jsonPath.split("..") #should be '/'
        print(pathElements)
        numOfElements = len(pathElements)
        fileToOpen = ".." + pathElements[numOfElements - 1] #gives ../documents/test.json when it should only be test.json
        print(fileToOpen)
        with open(fileToOpen) as json_file:
            jsonData = json.load(json_file)
    
        inputSplit = pathElements[numOfElements - 1].split("/") #should be '.'
        print(inputSplit) #should give something like ['test', 'json'] after splitting with '.' but because we have to split with '/' it gives ['', 'documents', 'test.json']
        #next 3 lines are extra steps that will be taken out but are necessary right now until naming issue is fixed
        tempLength = len(inputSplit)
        temp = inputSplit[tempLength - 1]
        temp2 = temp.split(".")
        fileName = temp2[0] + ".csv" #should be inputSplit[0]
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
        #destinationPath = parentpath + "/documents/" + fileName
        db.addFile(fileName) #doesn't save it to correct directory but it saves
        print("success!")
        os.chdir("../src")
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

# convertToJson("../documents/test.csv", "../documents/test.csv")
# uploadDocument("test2.json", "new2.json")
