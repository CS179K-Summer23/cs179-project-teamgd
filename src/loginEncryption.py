#pip install cryptography
from cryptography.fernet import Fernet

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
 with open('login.txt', 'r') as usernameConfirm:
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
    if passwordLines[usernameIndex].strip('\n') == password:
     loginInfo.close()
     return(True)
  loginInfo.close()
  return(False)


def deleteUser(username):
 with open('login.txt', 'r') as loginInfo:
  lines = loginInfo.readlines()
 for usernameLine in lines:
  if usernameLine.strip('\n') == username:
   passIndex = lines.index(usernameLine)
 loginInfo.close()
 with open('login.txt', 'w') as loginInfo:
  flag = True
  for line in lines:
   if line.strip('\n') != username and flag:
    loginInfo.write(line)
   elif not flag:
    flag = True
   if line.strip('\n') == username:
    flag = False
 loginInfo.close()


def loginEncrypt():
 with open('filekey.key', 'rb') as filekey:
  key = filekey.read()
 fernet = Fernet(key)

 with open('login.txt', 'rb') as loginInfo:
  original = loginInfo.read()

 encrypted = fernet.encrypt(original)
 with open('login.txt', 'wb') as encryptedFile:
  encryptedFile.write(encrypted)

 filekey.close()
 loginInfo.close()
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
  if len(lines) == 0:
   createLogin("test", "test")
   loginEncrypt()
  if len(lines) > 1:
   loginEncrypt()
  loginCheck.close()