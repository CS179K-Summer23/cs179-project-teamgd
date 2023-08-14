from datetime import datetime
import os
import json

currentpath = os.getcwd()
parentpath = os.path.dirname(currentpath)
documentpath = parentpath + "/documents/"

documentlist = []

class DataStat:
    def __init__(self, name, extension, wordcount, filesize, tcreated, taccessed):
        self.name = name
        self.extension = extension
        self.wordcount = wordcount
        self.filesize = filesize
        self.tcreated = tcreated
        self.taccessed = taccessed
    def printStat(self):
        print(self.name, self.extension, self.wordcount, self.tcreated, self.taccessed, "\n")

def populateDataStat(filename):
    file = os.path.splitext(filename)
    file_name = str(file[0])
    file_extension = str(file[1])
    file_wordcount = wordCount(filename)
    file_filesize = str(os.path.getsize(filename))
    file_tcreated = createtime(filename)
    file_taccessed = lastaccessedtime(filename)
    print("File Name: " + file_name)
    print("File Extension: " + file_extension)
    print("Word Count: " + file_wordcount)
    print("File Size: " + file_filesize + " bytes")
    print("Time Created: " + file_tcreated)
    print("Time Accessed: " + file_taccessed)
    tempfile = DataStat(file_name, file_extension, file_wordcount, file_filesize, file_tcreated, file_taccessed)
    # documentlist.append(tempfile)


def createtime(filename):
    timecreated = os.path.getctime(filename)
    datecreated = datetime.fromtimestamp(timecreated)
    createtime = str(datecreated)

    return createtime

def lastaccessedtime(filename):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # print("It is currently: ", current_datetime)
    
    currenttime = str(current_datetime)
    
    return currenttime

def wordCount(filename):
    wordnum = 0
    with open(filename) as file:
        content = file.read()
        lines = content.split()
        wordnum += len(lines)
    strwordnum = str(wordnum)
    return strwordnum

# populateDataStat(parentpath + "/documents/text.txt")

with open(parentpath + "/data/documentstats.json", "w") as outfile:
    for DataStat in documentlist:
        outfile.write(json.dumps(DataStat.__dict__, indent=4))

# def printFileStatistics(filename):
#     datafile = parentpath + "/data/test.json"
#     f = open(datafile, 'a')
#     f.write("File Name: ")
#     # print("File Name: ")
#     f.write(filename)
#     # print(filename)
#     f.write("\n")
#     f.close()
#     getExt(filename)
#     wordCount(filename, datafile)
#     timeStat(datafile)
# # 
# def startfile():
#     datafile = parentpath + "/data/test.json"
#     f = open(datafile, 'w')
#     f.close()
# startfile()    

