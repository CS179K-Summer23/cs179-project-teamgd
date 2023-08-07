#pip install cryptography
from cryptography.fernet import Fernet

def usernameQuery():
 print("Input a username > ", end = "")
 newUsername = input()
 usernameCheck(newUsername)


def usernameCheck(newUsername):
 with open('login.txt', 'r') as usernameConfirm:
  lines = usernameConfirm.readlines()
  for usernameLine in lines[::2]:
   if usernameLine == newUsername + "\n":
    print("Username is invalid. Please provide different username.")
    usernameQuery()
    return
  print("Creating new username...")
  usernameConfirm.close()
  passwordQuery(newUsername)


def passwordQuery(newUsername):
 print("Input a password > ", end = "")
 newPassword = input()
 print("Creating new password...")
 createLogin(newUsername, newPassword)


def createLogin(newUsername, newPassword):
 appendInput(newUsername)
 appendInput(newPassword)


def appendInput(userInput):
 with open('login.txt', 'a') as loginKey:
  loginKey.write(str(userInput))
  loginKey.write("\n")
  loginKey.close()


def login(username, password):
 with open('login.txt', 'r') as loginInfo:
  lines = loginInfo.readlines()
  usernameLines = lines[::2]
  passwordLines = lines[1::2]
  for usernameLine in usernameLines:
   if usernameLine == username + "\n":
    usernameIndex = usernameLines.index(usernameLine)
    if passwordLines[usernameIndex] == password + "\n":
     loginInfo.close()
     return(True)
  loginInfo.close()
  return(False)


def loginEncrypt():
 with open('filekey.key', 'rb') as filekey:
  key = filekey.read()
 fernet = Fernet(key)

 with open('login.txt', 'rb') as file:
  original = file.read()

 encrypted = fernet.encrypt(original)
 with open('login.txt', 'wb') as encryptedFile:
  encryptedFile.write(encrypted)

 filekey.close()
 file.close()
 encryptedFile.close()


def loginDecrypt():
 with open('filekey.key', 'rb') as filekey:
  key = filekey.read()
 fernet = Fernet(key)

 with open('login.txt', 'rb') as encryptedFile:
  encrypted = encryptedFile.read()

 original = fernet.decrypt(encrypted)
 with open('login.txt', 'wb') as file:
  file.write(original)

 filekey.close()
 encryptedFile.close()
 file.close()

def encryptCheck():
 with open('login.txt', 'r') as loginCheck:
  lines = loginCheck.readlines()
  loginCheck.close()
  if len(lines) == 0:
   createLogin("test", "test")
   loginEncrypt()
  if len(lines) > 1:
   loginEncrypt()