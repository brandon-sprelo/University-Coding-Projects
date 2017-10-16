def createAlphabet():
    alphabet = ''
    for i in range(32, 127):
        alphabet += str(chr(i))
    return alphabet

def createBinKeyFromKey(key):
    s = bin(key)
    t = s.split('b')
    binKey = t[1]
    return binKey

def encryptCS8Cipher(plainText, key):
    alpha = createAlphabet()
    a = createBinKeyFromKey(key)
    while len(a) < len(plainText):
        a += a
    x = ''
    for u in range(len(plainText)):
        if int(a[u]) == 1:
            idx = alpha.find(plainText[u])
            newCh = (alpha[(idx - key) % len(alpha)])
            x += newCh
        if int(a[u]) == 0:
            idx = alpha.find(plainText[u])
            newCh = alpha[(idx + key) % len(alpha)]
            x += newCh
    return x


def decryptCS8Cipher(plainText, key):
    alpha = createAlphabet()
    a = createBinKeyFromKey(key)
    while len(a) < len(plainText):
        a += a
    x = ''
    for u in range(len(plainText)):
        if int(a[u]) == 1:
            idx = alpha.find(plainText[u])
            newCh = (alpha[(idx + key) % len(alpha)])
            x += newCh
        if int(a[u]) == 0:
            idx = alpha.find(plainText[u])
            newCh = alpha[(idx - key) % len(alpha)]
            x += newCh
    return x


                
