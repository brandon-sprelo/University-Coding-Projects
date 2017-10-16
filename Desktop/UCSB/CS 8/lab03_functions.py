import random
import hist
import math

def coinFlipTrial(M, N):
    H = 0
    for i in range(N):
        heads = random.randrange(0, 2)
        if heads == 0:
            H += 1
    if H >= M:
        return True
    else:
        return False

def coinFlipExperiment(M, N, nTrials):
    L = 0
    for j in range(nTrials):
        if coinFlipTrial(M, N) == True:
            L += 1
    print ('probability =', L/nTrials * 100, '%')

def randomWalkFirstPassageTrial(D):
    'count is the amount of times it takes to get past D'
    x = 0
    y = 0
    count = 0
    while x**2 + y**2 < D**2:
        theta = random.uniform(0, 2 * math.pi)
        a = math.cos(theta)
        b = math.sin(theta)
        x += a
        y += b
        count += 1
    return count
        
def monteCarloRandomWalkFirstPassage(D, nTrials):
    L = 0
    K = []
    for i in range(nTrials):
        L += randomWalkFirstPassageTrial(D)
        K.append(randomWalkFirstPassageTrial(D))
    print('avSteps =', L / nTrials)
    hist.plotHistogram(K, binMin = 13, binMax = 827, nBins = 20)

def randomUniformSum(M):
    L = 0
    for i in range(M):
        L += random.uniform(0, M)
    return L / M
    
def plotRandomUniformSum(M, N, nBins):
    K = []
    for j in range(N):
        K.append(randomUniformSum(M))
    hist.plotHistogram(K, binMin = 0, binMax = M, nBins = nBins)
        
    




























        
        
