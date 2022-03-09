import string
import random
from cryptography.fernet import Fernet

DATA_FILE_PATH = "./data.txt"
ENCRYPTED_FILE_PATH = "./encrypted.txt"

def makeRandomString():
	stringLength=random.randrange(1, 30)
	randomString = ""
	for i in range(stringLength):
		randomString += str(random.choice(string.ascii_letters))
	return randomString

def fetchData():
	try:
		f = open(DATA_FILE_PATH, 'r')
	except:
		f = open(DATA_FILE_PATH, 'w')
		f.write(makeRandomString())
		f.close()
		f = open(DATA_FILE_PATH, 'r')
	data = f.read()
	f.close()
	return data

def encryptWithData(data):
	key = Fernet.generate_key()
	f = Fernet(key)
	return f.encrypt(bytes(data, 'utf-8'))

def savaEncrypted(token):
	f = open(ENCRYPTED_FILE_PATH, 'w')
	f.write(token.decode('utf-8'))
	f.close()

def readEncrypted():
	f = open(ENCRYPTED_FILE_PATH, 'r')
	data = f.read()
	f.close()
	return data


data = fetchData()
token = encryptWithData(data)
savaEncrypted(token)
readEncrypted = readEncrypted()
print(readEncrypted)




