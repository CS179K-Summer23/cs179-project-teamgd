import os

def deleteTestFiles():
    path = "./documents/"
    print(f"Files in the directory: {path}")
    
    files = os.listdir(path)
    files = [f for f in files if os.path.isfile(path+'/'+f)] #Filtering only the files.
    print(files)

    for i in range(len(files)):
        filepath = path + files[i]
        os.remove(filepath)



deleteTestFiles()