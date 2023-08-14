import random
import string
import sys
import csv
from database import *

num_txt_files = 10
num_json_files = 10
num_csv_files = 10

fileNameLength = random.randrange(8, 15)
textFileLength = random.randrange(100, 3000)

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
db = Database()


def generateTestFiles():
    generateTextFiles(num_txt_files)
    generateJsonFiles(num_json_files)
    generateCSVFiles(num_csv_files)
def generateCSVFiles(num_csv_files):
    for i in range(num_csv_files):
        name_set = string.ascii_letters + string.digits
        fileName = ''.join(random.choices(name_set, k=fileNameLength)) + ".csv"
        with open(parentpath + "/documents/" + fileName, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            header = []
            row1 = []
            row2 = []
            for j in range(4):
                header.append(random.randint(0, 9))
                row1.append(random.randint(0, 9))
                row2.append(random.randint(0, 9))
            writer.writerow(header)
            writer.writerow(row1)
            writer.writerow(row2)

        db.addFile(fileName)

def generateJsonFiles(num_json_files):
    for i in range(num_json_files):
        json_content_set = string.ascii_letters + string.digits
        fileName = ''.join(random.choices(json_content_set, k=fileNameLength)) + ".json"
        list = []

        for j in range(5):
            new_entry = {}
            for k in range(4):
                json_entry_name = ''.join(random.choices(json_content_set, k=5))
                json_entry_contents = ''.join(random.choices(json_content_set, k=20))
                new_entry[json_entry_name] = json_entry_contents
            list.append(new_entry)

        with open(parentpath + "/documents/" + fileName, "x") as f:
            f.write(json.dumps(list, indent=3))
            db.addFile(fileName)

def generateTextFiles(num_txt_files):
    for i in range(num_txt_files):
        name_set = string.ascii_letters + string.digits
        char_set = name_set + string.whitespace

        fileName = ''.join(random.choices(name_set, k=fileNameLength)) + ".txt"
        fileContents = ''.join(random.choices(char_set, k=textFileLength))

        f = open(parentpath + "/documents/" + fileName, "x")
        f.write(fileContents)
        db.addFile(fileName)


sys.path.insert(0, "./src")
generateTestFiles()