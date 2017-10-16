import string 
class Sentence:
    def __init__(self, s):
        self.s = str(s)
        self.L = s[:-1].split() 
        self.punctuation = s[-1]
    def getSentence(self):
        return self.s
    def getWords(self):
        return self.L
    def nChars(self):
        return len(self.s)
    def __len__(self):
        return len(self.L)
    def __getitem__(self, idx):
        return self.L[idx]
    def __setitem__(self, idx, word):
        self.L[idx] = word
        self.s = ' '.join(self.L) + self.punctuation
    def averageWordLength(self):
        self.avg = sum(len(i) for i in self.L)/len(self.L)
        return self.avg
    def minWordLength(self):
        return (min(len(i) for i in self.L))
    def maxWordLength(self):
        return (max(len(i) for i in self.L))
    def getPunctuation(self):
        return self.punctuation
    def setPunctuation(self, p):
        self.punctuation = p
        self.s = ' '.join(self.L) + p
    def capitalize(self):
        self.s = string.capwords(self.s) 
        self.L = self.s[:-1].split()
    def __add__(self, s2):
        self.count = len(s2[0])
        return (str(self.s[:-1]) + ', ' + str(s2[0].lower()) + s2.s[self.count:])
    def __str__(self):
        return str(self.s)
    
        
    
        
            
        
