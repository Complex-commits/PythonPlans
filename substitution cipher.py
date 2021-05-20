import pickle
import random


def main():
    cipher_dict = {
        'd':'a',
        'e':'f', 
        'h':'b', 
        'l':'p', 
        'l':'e', 
        'o':'j', 
        'r':'m', 
        'w':'i',
    }

    print(cipher_dict)

    print()

    #! Prints out the total number of items in the list/partial cipher.
    print(len(cipher_dict))

    print()

    #! Calls the program the display the cipher.
    print("TESTING PART 1")
    cipher = buildCipher()
    print(cipher)  # prints the cipher to the screen that the user can see.

    #@ Takes a message which is hello world and uses a cipher to encrypt the message.
    message = "hello world"
    encryptedMessage = encryptMessage(message, cipher)
    print(encryptedMessage)

    print("\nTesting Part 2")
    
    #@ Takes the encrypted message from part 1 and decrypts the cipher into a readble unaltered form.
    decryptedMessage = decrypt(encryptedMessage, cipher)
    print(decryptedMessage)

    #@ Takes the .data file and opens it to add that ecrypted data to the file.
    new_cipher = loadCipher("cipher.dat")
    print(decrypt(openEncryptedMessage(), new_cipher))


def openEncryptedMessage(filename="EncryptedMessage.txt"):
    #@ Opens the file that will store the encrypted message; makes it so that it returns/saves that content.
    infile = open(filename)
    contents = infile.read()
    infile.close()
    return contents

def buildCipher() -> dict:
    #@ This builds the Cesarian Cipher that is used to encrypt the message that will be printed out.
    dictionary = {}
    all_lettersinalphabet = "abcdefghijklmnopqrstuvwxyz"
    letterArray = []

    for i in range(26):
        letterArray.append(chr(97 + i))
    values = []


    for key in all_lettersinalphabet:
        match = False
        while match != True:
            randIndex = random.randrange(0, len(letterArray))
            if key != letterArray[randIndex]:
                values.append(letterArray[randIndex])
                letterArray.remove(letterArray[randIndex])
                match = True
    for i in range(26):
        dictionary[all_lettersinalphabet[i]] = values[i]
    return dictionary



def encryptMessage(text: str, cipher: dict):
    #@ This is the logic the function goes through when the user wants to encrypt the message.
    message = text.lower()
    messagesent = list(message)
    encryptMessagesArray = []

    for i in messagesent:
        if cipher.get(i):
            encryptMessagesArray.append(cipher.get(i))
        else:
            encryptMessagesArray.append(i)

    return ''.join(map(str, encryptMessagesArray))




def loadCipher(fileName: str):
    #@ This loads the cipher file and pickles it.
    pickle_in = open(fileName, "rb")
    dictionaryfrompickle = pickle.load(pickle_in)
    return dictionaryfrompickle


def decrypt(text: str, cipher: dict):
    #@ This function when it is called logically steps through the program and decrypts the encoded message.
    decryptmessage = text.lower()
    messagesdecrypt = list(decryptmessage)
    decrypt = []
    alphakeylist = list(cipher.values())

    for i in messagesdecrypt:    
        for c in cipher.items():
            if c[1] == i:
                decrypt.append(c[0])
                break
            elif c[1] == alphakeylist[-1]:
                decrypt.append(i)
    return ''.join(map(str, decrypt))



if __name__ == '__main__':
    main()
