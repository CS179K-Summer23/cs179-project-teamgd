from loginEncryption import getPath, loginEncrypt, loginDecrypt
from cryptography.fernet import Fernet
import os

def changeUsername(oldUsername, newUsername):
 path = getPath("login.txt")
 with open(path, 'w') as loginInfo:
  lines = loginInfo.readlines()
 index = 0
 for line in lines:
  if line.strip("\n") == oldUsername and index % 2 == 0:
   loginInfo.write(newUsername)
   loginInfo.write("\n") 
  else:
   loginInfo.write(line)
  index += 1
 loginInfo.close()


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


def securityQuestionCheck(inputUsername):
 path = getpath("security.txt")
 with open(path, 'r') as security:
  lines = security.readlines()
 usernames = lines[::3]
 for username in usernames:
  if username.split('\n') == inputUsername:
   return True
 return False


def addSecurityQuestion(username, questionOne, questionTwo):
 appendQuestion(username)
 appendQuestion(questionOne)
 appendQuestion(questionTwo)


def appendQuestion(userInput):
 path = getPath("security.txt")
 with open(path, 'a') as security:
  security.write(str(userInput))
  security.write("\n")
 security.close()


def changeSecurityQuestion(username, questionOne, questionTwo):
 path = getPath("security.txt")
 with open(path, 'r') as securityRead:
  lines = security.readlines()
 securityRead.close()
 index = 0
 with open(path, 'w') as security:
  for line in lines:
   if line.split('\n') == username:
    userindex = index
    security.write(line)
   elif index == (userindex + 1):
    security.write(questionOne)
    security.write("\n")
   elif index == (userindex + 2):
    security.write(questionTwo)
    security.write("\n")
   else:
    security.write(line)
   index += 1
 security.close()


def deleteSecurityQuestion(username):
 path = getPath("security.txt")
 with open(path, 'r') as securityRead:
  lines = security.readlines()
 securityRead.close()
 index = 0
 userindex = 1000
 with open(path, 'w') as security:
  for line in lines:
   if line.split('\n') == username:
    userindex = index
   elif index == (userindex + 1) or index == (userindex + 2):
    pass
   else:
    security.write(line)
   index += 1
 security.close()


def securityEncryptCheck():
 path = getPath("security.txt")
 with open(path, 'r') as securityCheck:
  lines = securityCheck.readlines()
  if len(lines) == 0:
   addSecurityQuestion("test","Question1 (answer is test):test", "Question2 (answer is test):test")
   loginEncrypt("security")
  if len(lines) > 1:
   loginEncrypt("security")
  securityCheck.close()