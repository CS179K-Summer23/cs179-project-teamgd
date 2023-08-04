import random
import string

def generateTestFiles():
    numFiles = 20
    for i in range(numFiles):
        fileNameLength = random.randrange(5, 20)
        fileLength = random.randrange(50, 1500)
        name_set = string.ascii_letters + string.digits
        char_set = string.printable

        fileName = ''.join(random.choices(name_set, k=fileNameLength))
        fileContents = ''.join(random.choices(char_set, k=fileLength))

        f = open("./documents/" + fileName + ".txt", "x")
        f.write(fileContents)


generateTestFiles()