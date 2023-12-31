#pip install cryptography
from cryptography.fernet import Fernet
import os

def getPath(document):
 currentpath = os.getcwd()
 parentpath = os.path.dirname(currentpath)
 documentpath = parentpath + "/data/"
 return(documentpath + str(document))

def usernameQuery():
 while(True):
  newUsername = input("Input a username > ")
  if usernameCheck(newUsername):
   print("Creating new username...")
   passwordQuery(newUsername)
   return newUsername
  else:
   print("Username is invalid. Please provide different username.")

def usernameCheck(newUsername):
 path = getPath("login.txt")
 with open(path, 'r') as usernameConfirm:
  lines = usernameConfirm.readlines()
  for usernameLine in lines[::2]:
   if usernameLine.strip('\n') == newUsername:
    return(False)
  return(True)

def getPassword(username):
 path = getPath("login.txt")
 with open(path, 'r') as loginInfo:
  lines = loginInfo.readlines()
 loginInfo.close()
 return lines[((lines[::2].index(username + "\n") * 2) + 1)].strip("\n")

def passwordQuery(newUsername):
 newPassword = input("Input a password > ")
 print("Creating new password...")
 createLogin(newUsername, newPassword)

def createLogin(newUsername, newPassword):
 appendInput(newUsername)
 appendInput(newPassword)
 createProfile(newUsername)

def appendInput(userInput):
 path = getPath("login.txt")
 with open(path, 'a') as loginKey:
  loginKey.write(str(userInput))
  loginKey.write("\n")
 loginKey.close()

def login(username, password):
 path = getPath("login.txt")
 with open(path, 'r') as loginInfo:
  lines = loginInfo.readlines()
  usernameLines = lines[::2]
  passwordLines = lines[1::2]
  for usernameLine in usernameLines:
   if usernameLine == username + "\n":
    usernameIndex = usernameLines.index(usernameLine)
    if passwordLines[usernameIndex].strip('\n') == password:
     loginInfo.close()
     return True 
  loginInfo.close()
  return False 

def createProfile(username): 
 currentpath = os.getcwd()
 parentpath = os.path.dirname(currentpath)
 profilepath = parentpath + "/data/docinfo" + username + ".json"
 if not os.path.exists(profilepath):
  with open(profilepath, 'w') as newFile:
   pass
 else:
  print("User already has a profile associated in the database!")

def loginEncrypt(filename):
 path = getPath(str(filename) + ".txt")
 keyPath = getPath("filekey.key")
 with open(keyPath, 'rb') as filekey:
  key = filekey.read()
 fernet = Fernet(key)
 with open(path, 'rb') as loginInfo:
  original = loginInfo.read()
 encrypted = fernet.encrypt(original)
 with open(path, 'wb') as encryptedFile:
  encryptedFile.write(encrypted)
 filekey.close()
 loginInfo.close()
 encryptedFile.close()

def loginDecrypt(filename):
 path = getPath(str(filename) + ".txt")
 keyPath = getPath("filekey.key")
 with open(keyPath, 'rb') as filekey:
  key = filekey.read()
 fernet = Fernet(key)
 with open(path, 'rb') as encryptedFile:
  encrypted = encryptedFile.read()
 original = fernet.decrypt(encrypted)
 with open(path, 'wb') as file:
  file.write(original)
 filekey.close()
 encryptedFile.close()
 file.close()

def encryptCheck():
 path = getPath("login.txt")
 with open(path, 'r') as loginCheck:
  lines = loginCheck.readlines()
  if len(lines) == 0:
   createLogin("test", "test")
   loginEncrypt("login")
  if len(lines) > 1:
   loginEncrypt("login")
  loginCheck.close()
