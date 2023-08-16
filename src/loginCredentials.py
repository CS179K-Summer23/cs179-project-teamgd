from loginEncryption import getPath, loginEncrypt, loginDecrypt
from cryptography.fernet import Fernet
import os

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