with open('ciphertext.txt', 'r') as file:
    cipher = file.read().strip()

def railDecrypt(cipherText, numRails):
    railLen = len(cipherText) // numRails
    solution = ''
    for col in range(railLen):
        for rail in range(numRails):
            nextLetter = col + (rail * railLen)
            if nextLetter < len(cipherText):
                solution += cipherText[nextLetter]
    return solution.split()  # Returns words

def createWordDict(dName):
    myDictionary = {}
    with open(dName, 'r') as myFile:
        for line in myFile:
            word = line.strip()
            if word:
                myDictionary[word.lower()] = True
    return myDictionary

def railBreak(cipherText, numRails, dictionary):
    decryptedWords = railDecrypt(cipherText, numRails)
    validWordCount = sum(1 for word in decryptedWords if word.lower() in dictionary)
    totalWords = len(decryptedWords)

    return ' '.join(decryptedWords)

# calls
dictionary = createWordDict("words.txt")
result = railBreak(cipher, 4, dictionary)
print(result)
