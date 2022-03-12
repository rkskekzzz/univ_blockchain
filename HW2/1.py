from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def getUserInput():
	return input()

def getPrivateKey():
	with open("private_key.pem", 'rb') as private_key_file:
		private_key = serialization.load_pem_private_key(
			private_key_file.read(),
			password=None,
		)
	return private_key

def getPublicKey():
	with open("public_key.pem", 'rb') as public_key_file:
		public_key = serialization.load_pem_public_key(
			public_key_file.read(),
		)
	return public_key

def getPlainFile(): # for Debug
	with open("tail.txt", 'rb') as plain_file:
		plain_message = plain_file.read()
	return plain_message


def encryptWithRSA(plain_message, public_key):
	encrypted_message = public_key.encrypt(
		plain_message,
		padding.OAEP(
			mgf=padding.MGF1(algorithm=hashes.SHA256()),
			algorithm=hashes.SHA256(),
			label=None
		)
	)
	return encrypted_message

def encryptWithAES(plain_message, public_key):
	aes_key = Fernet.generate_key()
	f = Fernet(aes_key)
	encrypted_message = f.encrypt(plain_message)
	encrypted_aes_key = encryptWithRSA(aes_key, public_key)
	return {'encrypted_aes_key': encrypted_aes_key, 'encrypted_message': encrypted_message}

def decryptWithRSA(encrypted_message, private_key):
	plain_msg = private_key.decrypt(
		encrypted_message,
		padding.OAEP(
			mgf=padding.MGF1(
				algorithm=hashes.SHA256()),
				algorithm=hashes.SHA256(),
				label=None
			)
		)
	return plain_msg

def decryptWithAES(message, private_key):
	aes_key = decryptWithRSA(message['encrypted_aes_key'], private_key)
	f = Fernet(aes_key)
	return f.decrypt(message['encrypted_message'])

def getMessageAndDecrypt(message, private_key):
	if type(message) is bytes:
		plain_msg = decryptWithRSA(message, private_key)
	else:
		plain_msg = decryptWithAES(message, private_key)
	return plain_msg

def sender():
	user_input = getUserInput()
	public_key = getPublicKey()
	plain_message = getPlainFile() # n보다 큰 byte의 텍스트 테스트
	try:
		encrypted = encryptWithRSA(bytes(user_input, 'utf-8'), public_key)
	except:
		encrypted = encryptWithAES(bytes(user_input, 'utf-8'), public_key)
	return encrypted


def receiver(enc_msg):
	private_key = getPrivateKey()
	plain_msg = getMessageAndDecrypt(enc_msg, private_key)
	print(plain_msg)


enc_msg = sender()
print(enc_msg)
receiver(enc_msg)
