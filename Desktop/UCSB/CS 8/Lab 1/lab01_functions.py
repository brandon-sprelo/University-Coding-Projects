def pay(hourlyWage, nHours):
    if nHours <= 40:
        return hourlyWage * nHours
    elif 40 < nHours <= 60:
        return 40 * hourlyWage + 1.5 * (nHours - 40) * hourlyWage
    else:
        return 40 * hourlyWage + 1.5 * 20 * hourlyWage\
               + 2 * (nHours - 60) * hourlyWage
    
print (pay(10,35))
print (pay(10,45))
print (pay(10,61))

def statement(LTransactions):
    a = totalWithdrawals = 0
    b = totalDeposits = 0
    for x in LTransactions:
        if x < 0:
            a += x
        if x > 0:
            b += x
    return [a, b]

print(statement([30.95, -15.67, 45.56, -55.00, 43.78]))
print(statement([10, 20, 100]))

def countPrimes(N):
    L = 0
    for x in range(2, N + 1):
        prime = True
        for i in range(2, x):
            if x%i == 0:
                prime = False
        if prime:
            L += 1
    return L

def sumInversePrimes(N):
    acc = 0
    for x in range(2, N + 1):
        prime = True
        for i in range(2, x):
            if x%i == 0:
                prime = False
        if prime:
            acc = acc + 1 / x
    return acc












