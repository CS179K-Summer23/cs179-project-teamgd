import json
import csv
import os

def convertToJson(csvPath, jsonPath):
    data = {}
    index = 0
    
    with open(csvPath) as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            # key = rows['a'] 
            # data[key] = rows
            data[index] = rows
            index += 1
 
    with open(jsonPath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    print("Success")

# Takes from local computer to the database
def uploadDocument(srcPath, destPath):
    # reads file format and if its not json convert it to json
    split = os.path.splitext(srcPath)

    fileExtension = split[1]
    print(fileExtension)
    if fileExtension != '.json' and fileExtension == '.csv':
        print("Convertind from csv to json")
        convertToJson(srcPath, destPath)
    else:
        print("test")

uploadDocument("test2.csv", "new.json")