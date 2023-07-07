import math
import pandas as pd
def prime(x):
    res = []
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            while True:
                if x % i == 0:
                    res.append(i)
                    x /= i
                else:
                    break
            if x == 1:
                return res
    return [1,x]

def checkprime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True



n = int(input('n='))
for i in range(n+1,0,-1):
    if checkprime(i):
        print(i)
        break




           

           