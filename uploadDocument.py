def uploadDocument(fname):
    # DEpending on how the data is stored, read the file name and store it as that 
    f = open(fname, 'r+')
    print(f.read())
    f.close()

uploadDocument("test.txt")