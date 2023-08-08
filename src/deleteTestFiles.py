import os
from database import *

def deleteTestFiles():
    currentpath = os.getcwd()
    parentpath = os.path.dirname(currentpath)

    db = Database()

    path = parentpath + "/documents/"

    files = os.listdir(path)
    files = [f for f in files if os.path.isfile(path+'/'+f)] #Filtering only the files.

    for i in range(len(files)):
        filepath = path + files[i]
        db.deleteFile(fileName=files[i], docnum=-1)




deleteTestFiles()