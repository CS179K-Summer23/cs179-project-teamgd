import random
import string
import sys
from database import *

num_files = 20
min_file_length = 100
max_file_length = 3000

def generateTestFiles():

    currentpath = os.getcwd()
    parentpath = os.path.dirname(currentpath)
    db = Database()
    for i in range(num_files):
        fileNameLength = random.randrange(8, 15)
        fileLength = random.randrange(100, 3000)
        name_set = string.ascii_letters + string.digits
        char_set = string.printable

        fileName = ''.join(random.choices(name_set, k=fileNameLength)) + ".txt"
        fileContents = ''.join(random.choices(char_set, k=fileLength))

        f = open(parentpath + "/documents/" + fileName, "x")
        f.write(fileContents)
        db.addFile(fileName)



sys.path.insert(0, "./src")
generateTestFiles()