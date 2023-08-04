import os
from database import *

def deleteTestFiles():
    db = Database()
    path = "./documents/"
    
    files = os.listdir(path)
    files = [f for f in files if os.path.isfile(path+'/'+f)] #Filtering only the files.

    for i in range(len(files)):
        filepath = path + files[i]
        os.remove(filepath)
        db.deleteFile(files[i])




deleteTestFiles()