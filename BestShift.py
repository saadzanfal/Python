import string
def is_word(wordlist, word):
    
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    maxWords = 0
    bestShift = 0
    #apply all possible shifts to text
    for shift in range(0,26):
        #reset words to 0
        currentWords = 0
        code = applyShift(text, shift)
        strings = code.split()
        for i in range(len(strings)):
            #count valid words
            if is_word(wordList, strings[i]):
                currentWords = currentWords + 1
            if currentWords > maxWords:
                #choose shift that gives most valid words
                maxWords = currentWords
                bestShift = shift
    return (bestShift)
