import json
import csv

userInput = input("enter name of json file (must end with .json):\n")
length = len(userInput)
check = userInput[length - 5:]

if check == ".json": #based upon the assumption that the json file already exists within the respective database
    with open(userInput) as json_file:
        jsonData = json.load(json_file)
    
    inputSplit = userInput.split(".")
    fileName = inputSplit[0] + ".csv"
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
    
else:
    print("Unable to read input of json file, please try again.\n")
