import json

class Database:

    db = {}
    def __init__(self):
        with open("./data/docinfo.json") as f:
            self.db = json.load(f)
        i=0
        for doc in self.db['documents']:
            i=i+1
            doc['docnumber'] = i

    def printDocs(self):
        print("List of your documents: ")
        for doc in self.db['documents']:
            s = str(doc["docnumber"]) + ". " + doc["name"]
            print(s)

    def getDoc(self):
        print("Please type the number of the document you want to access")
        choice = int(input())
        #if choice > self.db['documents'].length:
        #    print("Invalid Input")
        #    return

        for doc in self.db['documents']:
            if choice == doc['docnumber']:
                return doc




    

            
        