import random
import string
import sys
from database import *



def generateTestFiles():
    db = Database()
    numFiles = 20
    for i in range(numFiles):
        fileNameLength = random.randrange(5, 20)
        fileLength = random.randrange(50, 1500)
        name_set = string.ascii_letters + string.digits
        char_set = string.printable

        fileName = ''.join(random.choices(name_set, k=fileNameLength)) + ".txt"
        fileContents = ''.join(random.choices(char_set, k=fileLength))

        f = open("./documents/" + fileName, "x")
        f.write(fileContents)
        db.addFile(fileName)



sys.path.insert(0, "./src")
generateTestFiles()