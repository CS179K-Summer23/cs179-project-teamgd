from datetime import datetime

def currentTime(datafile):
    current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    # print("It is currently: ", current_datetime)
    
    currenttime = str(current_datetime)
    
    # open passed in file name
    f = open(datafile, 'a')
    f.write("Last Accessed: ")
    f.write(current_datetime)
    f.write("\n \n")
    f.close()

def wordCount(filename, datafile):
    wordnum = 0
    with open(filename) as file:
        content = file.read()
        lines = content.split()
        wordnum += len(lines)
        f = open(datafile, 'a')
        f.write("Wordcount: ")
        f.write(str(wordnum))
        f.write("\n")
        f.close()
        
def printFileStatistics():
    datafile = "../data/test.json"
    filename = "../documents/text.txt"
    f = open(datafile, 'a')
    f.write("File Name: ")
    f.write(filename)
    f.write("\n")
    f.close()
    wordCount(filename, datafile)
    currentTime(datafile)
    
printFileStatistics()