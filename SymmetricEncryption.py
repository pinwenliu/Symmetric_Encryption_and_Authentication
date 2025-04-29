import os
import sys
import time
from Crypto.Cipher import AES
from cryptography.hazmat.primitives.ciphers.aead import AESCCM
from cryptography.hazmat.primitives.ciphers.modes import CTR
from Crypto.Cipher import ChaCha20
from Crypto.Hash import SHA3_512
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# 加密檔案
def AESCCM_encrypt(key, data, nonce): #使用AES-CCM mode加密
	start = time.time()
	aesccm = AESCCM(key)   
	encryptData = aesccm.encrypt(nonce, data, None)   
	end = time.time()
	total_time = end - start

	return encryptData,total_time

def AESCTR_encrypt(key, data, iv): #使用AES-CTR mode (counter mode)加密
	start = time.time()    
	cipher = Cipher(algorithms.AES(key), modes.CTR(iv))
	encryptor = cipher.encryptor()
	encryptData = encryptor.update(data) + encryptor.finalize()
	end = time.time()
	total_time = end - start

	return encryptData,total_time   

def ChaCha20_encrypt(key, data, nonce):   #使用ChaCha20加密
	start = time.time()      
	algorithm = algorithms.ChaCha20(key, nonce)
	cipher = Cipher(algorithm, mode=None)
	encryptor = cipher.encryptor()
	encryptData = encryptor.update(data)
	end = time.time()
	total_time = end - start
	return encryptData,total_time
	
# 解密檔案
def AESCCM_decrypt(key, data, nonce):	#使用AES-CCM mode解密
	aesccm = AESCCM(key)   
	decryptData = aesccm.decrypt(nonce, data, None) 

	return decryptData

def AESCTR_decrypt(key, data, iv): #使用AES-CTR mode (counter mode)解密
	cipher = Cipher(algorithms.AES(key), modes.CTR(iv))	
	decryptor = cipher.decryptor()
	decryptData = decryptor.update(data) + decryptor.finalize()

	return decryptData  

def ChaCha20_decrypt(key, data, nonce):	#使用ChaCha20解密
	algorithm = algorithms.ChaCha20(key, nonce)
	cipher = Cipher(algorithm, mode=None)
	decryptor = cipher.decryptor()
	decryptData = decryptor.update(data)

	return decryptData   

def hash(string):	#cryptographic hashes
    h = SHA3_512.new()
    h.update(string.encode())
    return h.hexdigest()

if __name__ == "__main__":

	##### 1. 請使用加密相關的library，實作加密檔案的程式(檔案需至少100MB)。#####

	# read file
	with open('secretFile.txt', 'rb') as f:
		data = f.read()
		dataSize = os.path.getsize('secretFile.txt')
		print('the size of the file:', dataSize, ' bytes')

	key = AESCCM.generate_key(bit_length=256) #產生256bytes的key
	iv =  os.urandom(16) #亂數產生16bytes的iv
	AESCCM_nonce = os.urandom(7) #亂數產生7bytes的nonce
	ChaCha20_nonce = os.urandom(16) #亂數產生7bytes的nonce

	#AES-CCM encrypt
	AESCCM_encryptData,AESCCM_time = AESCCM_encrypt(key, data, AESCCM_nonce)
	AESCCM_CipherFile = open("AESCCM_CipherFile.txt","wb")
	AESCCM_CipherFile.write(AESCCM_encryptData)
	print('speed of AES-CCM encryption: ', str(dataSize/AESCCM_time), 'bytes/s')
	
	#AES-CTR encrypt
	AESCTR_encryptData,AESCTR_time = AESCTR_encrypt(key, data, iv)
	AESCTR_CipherFile = open("AESCTR_CipherFile.txt","wb")
	AESCTR_CipherFile.write(AESCTR_encryptData)
	print('speed of AES-CTR encryption: ', str(dataSize/AESCTR_time), 'bytes/s')

	#ChaCha20 encrypt
	ChaCha20_encryptData,ChaCha20_time = ChaCha20_encrypt(key, data, ChaCha20_nonce)
	ChaCha20_CipherFile = open("ChaCha20_CipherFile.txt","wb")
	ChaCha20_CipherFile.write(ChaCha20_encryptData)
	print('speed of ChaCha20 encryption: ', str(dataSize/ChaCha20_time), 'bytes/s')

	#AES-CCM decrypt
	AESCCM_decryptData = AESCCM_decrypt(key, AESCCM_encryptData, AESCCM_nonce)
	AESCCM_PlaintFile = open("AESCCM_PlaintFile.txt","w")
	AESCCM_PlaintFile.write(str(AESCCM_decryptData))
	
	#AES-CTR decrypt
	AESCTR_decryptData = AESCTR_decrypt(key, AESCTR_encryptData, iv)
	AESCTR_PlaintFile = open("AESCTR_PlaintFile.txt","w")
	AESCTR_PlaintFile.write(str(AESCTR_decryptData))

	#ChaCha20 decrypt
	ChaCha20_decryptData = ChaCha20_decrypt(key, ChaCha20_encryptData, ChaCha20_nonce)
	ChaCha20_PlaintFile = open("ChaCha20_PlaintFile.txt","w")
	ChaCha20_PlaintFile.write(str(ChaCha20_decryptData))

	# Vertify the result of implemetations
	print('Is the implementation of AES-CCM encryption and decryption correct?')
	if (AESCCM_decryptData == data):
		print('Correct!')
	else:
		print('Incorrect!')

	print('\nIs the implementation of AES-CTR encryption and decryption correct?')
	if (AESCTR_decryptData == data):
		print('Correct!')
	else:
		print('Incorrect!')

	print('\nIs the implementation of ChaCha20 encryption and decryption correct?')
	if (ChaCha20_decryptData == data):
		print('Correct!')
	else:
		print('Incorrect!')

	print('')
	#####2. 請計算出"I love cryptography." 這個字串（不含雙引號）的SHA-3-512 message digest#####
	#cryptographic hashes
	string = "I love cryptography."  
	print('The digest of \"', string, '\" : ', hash(string))