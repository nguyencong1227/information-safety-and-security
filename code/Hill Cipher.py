# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 07:26:13 2022

@author: ADMIN
"""
import numpy as np
# Python3 code to implement Hill Cipher

# Python3 code to implement Hill Cipher

keyMatrix = [[0] * 3 for i in range(3)]
de_key = [[0] * 3 for i in range(3)]
# Generate vector for the message
messageVector = [[0] for i in range(3)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]
PlainMatrix = [[0] for i in range(3)]
# Following function generates the
# key matrix for the key string

# Function to group 2 elements of a string
# as a list element


def Diagraph(text):
	Diagraph = []
	group = 0
	for i in range(3, len(text), 3):
		Diagraph.append(text[group:i])

		group = i
	Diagraph.append(text[group:])
	return Diagraph


def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

# Following function encrypts the message
def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26
            
def decrypt(messageVector):
	for i in range(3):
		for j in range(1):
			PlainMatrix[i][j] = 0
			for x in range(3):
				PlainMatrix[i][j] += (de_key[i][x] *
									messageVector[x][j])
			PlainMatrix[i][j] = PlainMatrix[i][j] % 26

def HillCipher(message, key):

	# Get key matrix from the key string
    getKeyMatrix(key)
    de_key = np.linalg.inv(keyMatrix)
	# Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

	# Following function generates
	# the encrypted vector
    encrypt(messageVector)

	# Generate the encrypted text
	# from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))
    Plaintext = []
    for i in range(3):
        Plaintext.append(chr(PlainMatrix[i][0] + 65))
	# Finally print the ciphertext
    print("Ciphertext: ", "".join(CipherText))
    print("Plaintext: ", "".join(Plaintext))
    
    

# Driver Code
def main():

	# Get the message to
	# be encrypted
    message = "ACTACT"
    message = Diagraph(message)
    if len(message[-1]) != 3:
        print("Nhập lại massage")
	# Get the key
    key = "GYBNQKURP"
    for i in message:
        HillCipher(i, key)

if __name__ == "__main__":
	main()
