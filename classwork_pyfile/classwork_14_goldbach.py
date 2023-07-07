import math

def checkprime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

n = eval(input('n='))
for n1 in range(2, n-1):
    if checkprime(n1):
        n2 = n - n1
        if checkprime(n2):
            print('n1: ' + str(n1) + '\tn2: ' + str(n2))

