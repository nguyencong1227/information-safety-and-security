def charToNum(char):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    num = 1
    for letter in alphabet:
        if letter == char:
            break
        else:
            num+=1
    return num


def numToChar(num):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[num+1]

def encodeChar(pText, key):
    cNum = ( charToNum(pText) + charToNum(key) ) % 26
    cText = numToChar(cNum)
    return cText

def decodeChar(cText, key):
    pNum = charToNum(cText) - charToNum(key)
    pText= numToChar(pNum)
    return pText


def encode(pText, key):
    cText= ""
    for i in range(0, len(pText)):
        cText += encodeChar(pText[i], key[i])

    return cText

def decode(cText, key):
    pText=""
    for i in range(0, len(cText)):
        pText += decodeChar(cText[i], key[i])
    return pText

def main():
    cont=True
    choice=""
    print("OTP Program.  Key must be less than or equal to plaintext in length.  Plaintext must not contain numbers.")
    print("\nChoices:\n1: Encode\n2: Decode\n3: Quit")
    while cont == True:
        choice = input(">>> ")
        if choice == "1":
            print("Your ciphertext is " + encode(input("Please enter your plaintext: "), input("Please enter your key: ")))

        elif choice == "2":
            print("Your plaintext is " + decode(input("Please enter your ciphertext: "), input("Please enter your key: ")))

        elif choice == "3":
            cont = False

        else:
            print("Please choose 1, 2, or 3")

main()