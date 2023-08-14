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
  print("Input a username > ", end = "")
  newUsername = input()
  if usernameCheck(newUsername):
   print("Creating new username...")
   passwordQuery(newUsername)
   return
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


def passwordQuery(newUsername):
 print("Input a password > ", end = "")
 newPassword = input()
 print("Creating new password...")
 createLogin(newUsername, newPassword)


def createLogin(newUsername, newPassword):
 appendInput(newUsername)
 appendInput(newPassword)


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
     return(True)
  loginInfo.close()
  return(False)


def changePassword(username, newPassword):
 path = getPath("login.txt")
 with open(path, 'r') as loginInfo:
  lines = loginInfo.readlines()
 loginInfo.close()
 with open(path, 'w') as loginInfo:
  index = 0
  flag = True
  for line in lines:
   if not flag:
    loginInfo.write(newPassword)
    loginInfo.write("\n")
    flag = True
   else:
    loginInfo.write(line)
   if line.strip('\n') == username and index % 2 == 0:
    flag = False
   index += 1
 loginInfo.close()


def deleteUser(username):
 path = getPath("login.txt")
 with open(path, 'r') as loginInfo:
  lines = loginInfo.readlines()
 loginInfo.close()
 with open(path, 'w') as loginInfo:
  index = 0
  flag = True
  for line in lines:
   if (line.strip('\n') != username or index % 2 == 1) and flag:
    loginInfo.write(line)
   elif not flag:
    flag = True
   if line.strip('\n') == username and index % 2 == 0:
    flag = False
   index += 1
 loginInfo.close()


def adminCheck(password):
 loginDecrypt("admin")
 path = getPath("admin.txt")
 with open(path, 'r') as adminInfo:
  lines = adminInfo.readlines()
 adminInfo.close()
 for line in lines:
  if password == line.strip('\n'):
   loginEncrypt("admin")
   return True
 loginEncrypt("admin")
 return False


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
   loginEncrypt()
  if len(lines) > 1:
   loginEncrypt("login")
  loginCheck.close()