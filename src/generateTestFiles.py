import random
import string
import sys
import csv
from database import *
from randomwords import *

doc_count = 0

num_txt_files = 10
num_json_files = 10
num_csv_files = 10
num_nested_json_files = 10

dict_length = 3
list_length = 3
nested_height = 4

fileNameLength = random.randrange(8, 15)
textFileLength = random.randrange(50, 300)

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
db = Database()

random_words = getRandomWords()


def generateTestFiles():
    generateTextFiles(num_txt_files)
    generateJsonFiles(num_json_files)
    generateCSVFiles(num_csv_files)
    generateNestedJsonFiles(num_nested_json_files)
def generateCSVFiles(num_csv_files):
    row_length = 10
    col_length = 10
    min_int = -100
    max_int = 100
    for i in range(num_csv_files):
        fileName = ''.join(random.choices(string.ascii_letters + string.digits, k=fileNameLength)) + ".csv"
        with open(parentpath + "/documents/" + fileName, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            header = []
            for j in range(col_length):
                row = []
                for k in range(row_length):
                    row.append(random.choice(random_words))
                writer.writerow(row)
            db.addFile(fileName)

def generateJsonFiles(num_json_files):
    for i in range(num_json_files):
        json_content_set = string.ascii_letters + string.digits
        fileName = ''.join(random.choices(string.ascii_letters + string.digits, k=fileNameLength)) + ".json"
        list = []

        for j in range(5):
            new_entry = {}
            for k in range(4):
                json_entry_name = random.choice(random_words)
                json_entry_contents = random.choice(random_words)
                new_entry[json_entry_name] = json_entry_contents
            list.append(new_entry)

        with open(parentpath + "/documents/" + fileName, "x") as f:
            f.write(json.dumps(list, indent=3))
            db.addFile(fileName)

def generateNestedJsonFiles(num_nested_json_files):
    for i in range(num_nested_json_files):
        fileName = ''.join(random.choices(string.ascii_letters + string.digits, k=fileNameLength)) + "_nested.json"
        dict = generatePythonDict()

        generateNestedJsonLevel(0, dict)

        with open(parentpath + "/documents/" + fileName, "x") as f:
            f.write(json.dumps(dict, indent=3))
            db.addFile(fileName)

def generateNestedJsonLevel(current_height, branch):
    if (current_height < nested_height):
        current_height = current_height+1

        if type(branch) is dict:
            # print("Initial Branch:" + str(branch))
            entries = branch.values()
            # print("Initial Entries:" + str(entries))
            for entry in list(branch.values()):
                if random.randint(0, 100) < 100:
                    if random.randint(0, 100) < 50:
                        branch[entry] = generatePythonList()
                    else:
                        # print("Current Branch: " + str(branch))
                        # print("Current Entries:" + str(entries))
                        # print("Entry Chosen: " + str(entry))
                        branch[entry] = generatePythonDict()
                        generateNestedJsonLevel(current_height, branch[entry])





def generatePythonDict():
    dict = {}
    for i in range(dict_length*2-1):
        json_entry_name = random.choice(random_words)
        json_entry_contents = random.choice(random_words)
        dict[json_entry_name] = json_entry_contents
    #print(dict)
    return dict

def generatePythonList():
    list = []
    words = random.choices(random_words, k=dict_length)
    for i in range (list_length):
        list.append(words[i])
    #print(list)
    return list

def generateTextFiles(num_txt_files):
    fileContents = ""
    for i in range(num_txt_files):
        name_set = string.ascii_letters + string.digits
        char_set = name_set + string.whitespace

        fileName = ''.join(random.choices(name_set, k=fileNameLength)) + ".txt"
        for i in range(textFileLength):
            fileContents = fileContents + random.choice(random_words)
            if random.randint(0, 100) < 10:
                fileContents = fileContents + "\n"
            fileContents = fileContents + " "

        f = open(parentpath + "/documents/" + fileName, "x")
        f.write(fileContents)
        db.addFile(fileName)



sys.path.insert(0, "./src")
generateTestFiles()
