letterPoints = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1,'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1,'s':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}


def createWordList(filename):
    file = open(filename, 'r')
    s = file.read()
    file.close()
    L = s.split('\n')
    return L[:-1]

def canWeMakeIt(myWord, myLetters):
    listY = []
    x = list(myWord)
    y = list(myLetters)
    for block in range(len(myLetters)):
        if y[block] in x:
            x.remove(y[block])
    if len(x) == 0:
        return True
    else:
        return False 
    
def getWordPoints(myWord, letterPoints):
    accumulator = 0
    for ch in myWord:
        accumulator += letterPoints[ch]
    return accumulator

def scrabbleWords(myLetters):
    wordList = createWordList('wordlist.txt')
    myWords = []
    for i in range(len(wordList)):
        if canWeMakeIt(wordList[i], myLetters) == True:
            myWords.append(wordList[i])
    pointWordList = []
    for q in myWords:
        pointValue = getWordPoints(q, letterPoints)
        pointWordList.append((pointValue, q))
    sortWordList = sorted(pointWordList, reverse=True)


    fmt = '{:' + str(len(myLetters)+4) + '} {} \n'
    s = ''
    for x,y in sortWordList:
        s += fmt.format(y,x)

    openfile = open('%s.txt'%myLetters, 'w')
    openfile2 = openfile.write(s)
    openfile.close()

    


    
    
    

    
        

    
    
