from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import serialization


def fetchData():
	res = input()
	return res

def getPrivateKey():
	with open("private_key.pem", 'rb') as privateKeyFile:
		privateKey = serialization.load_pem_private_key(
			privateKeyFile.read(),
			password=None,
		)
	return privateKey

def getPublicKey():
	with open("public_key.pem", 'rb') as publicKeyFile:
		publicKey = serialization.load_pem_public_key(
			publicKeyFile.read(),
		)
	return publicKey

# def encryptWithData(data):
# 	key = Fernet.generate_key()
# 	f = Fernet(key)
# 	return f.encrypt(bytes(data, 'utf-8'))

# def savaEncrypted(token):
# 	f = open(ENCRYPTED_FILE_PATH, 'w')
# 	f.write(token.decode('utf-8'))
# 	f.close()

# def readEncrypted():
# 	f = open(ENCRYPTED_FILE_PATH, 'r')
# 	data = f.read()
# 	f.close()
# 	return data


userInput = fetchData()
privateKey = getPrivateKey()
publicKey = getPublicKey()
print(privateKey, publicKey)
# token = encryptWithData(data)
# savaEncrypted(token)
# readEncrypted = readEncrypted()





