from loginEncryption import getPath, loginEncrypt, loginDecrypt
from cryptography.fernet import Fernet
import os
import re
import shutil

def changeUsername(oldUsername, newUsername):
 path = getPath("login.txt")
 with open(path, 'r') as loginInfo:
  lines = loginInfo.readlines()
 with open(path, 'w') as loginInfo:
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
 deleteProfile(username)


def deleteProfile(username):
 currentpath = os.getcwd()
 parentpath = os.path.dirname(currentpath)
 profilepath = parentpath + "/documents/" + username
 if os.path.exists(profilepath):
  try:
   shutil.rmtree(profilepath)
  except OSError as e:
   print(f"Error, {o.stderror}: {path}")
 else:
  print("User does not have an associated profile. This should not affect deletion process...")

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


def askQuestion(username):
 path = getPath("security.txt")
 with open(path, 'r') as security:
  lines = security.readlines()
 security.close()
 userIndex = lines.index((username + "\n"))
 print("\n" + lines[userIndex + 1].split(":")[0])
 answer = input("Provide an answer to this question > ")
 if(answer.lower() == lines[userIndex + 1].split(":")[1].strip("\n")):
  print("\n" + lines[userIndex + 2].split(":")[0])
  answer = input("Provide an answer to this question > ")
  if(answer.lower() == lines[userIndex + 2].split(":")[1].strip("\n")):
   return True
 return False


def securityQuestionCheck(inputUsername):
 path = getPath("security.txt")
 with open(path, 'r') as security:
  lines = security.readlines()
 security.close()
 usernames = lines[::3]
 for username in usernames:
  if inputUsername == username.strip("\n"):
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


def selectQuestion(questionList):
 num = 1
 print("\n------------------")
 print("List of Questions:")
 print("------------------")
 for question in questionList:
  print(str(num) + ": " + question)
  num += 1
 while True:
  selection = input("\nSelect a question to answer > ")
  try:
   selectQuestion = questionList[int(selection)-1]
   break
  except Exception:
   print("Input is invalid! Please select a valid number.")
 while True:
  print("\n" + selectQuestion)
  answer = input("Provide an answer to this question > ")
  if re.search("[^a-zA-Z0-9s]", answer):
   print("Please do not include special characters in your answer.")
  else:
   break
 modifiedAnswer = selectQuestion + ":" + answer.lower()
 del questionList[int(selection)-1]
 return modifiedAnswer, questionList
 

def changeSecurityQuestion(username, questionOne, questionTwo):
 path = getPath("security.txt")
 with open(path, 'r') as securityRead:
  lines = securityRead.readlines()
 securityRead.close()
 index = 0
 userindex = lines.index(username + "\n")
 with open(path, 'w') as security:
  for line in lines:
   if index == (userindex + 1):
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
  lines = securityRead.readlines()
 securityRead.close()
 index = 0
 userindex = lines.index(username + "\n")
 with open(path, 'w') as security:
  for line in lines:
   if username == line.strip("\n") or index == (userindex + 1) or index == (userindex + 2):
    pass
   else:
    security.write(line)
   index += 1
 security.close()


def getQuestionList():
 return(["What city were you born?", "What is your favorite sports team?", "What is the make and model of your first car?", "Where is your favorite place to vacation?", "What is your favorite food?", "What city did you attend university?", "What is your mother’s middle name?", "What is the name of the street that you grew up on?", "What is the first name of your best friend?", "What was the name of your first pet?"])


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
