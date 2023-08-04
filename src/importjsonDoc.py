import json
import csv
import os

def convertToJson(csvPath, jsonPath):
    data = {}
    index = 0
    
    with open(csvPath) as csvf:
        csvReader = csv.DictReader(csvf)
        for rows in csvReader:
            # Currently uses Arbitrary key 'index'
            data[index] = rows
            index += 1
 
    with open(jsonPath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
    
    # print("Success")

# Takes from local computer to the database
def uploadDocument(srcPath, destPath):
    split = os.path.splitext(srcPath)

    fileExtension = split[1]

    # reads file format if its not json convert it to json
    if fileExtension != '.json' and fileExtension == '.csv':
        # print("Converting from csv to json")
        convertToJson(srcPath, destPath)
    elif fileExtension == '.json':
        f = open(srcPath)
        data = json.load(f)
        with open(destPath, 'w') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
        f.close()
    else:
        print("File extension not recognized.")

uploadDocument("test2.csv", "./documents/new.json")
# uploadDocument("test.json", "./documents/new.json")