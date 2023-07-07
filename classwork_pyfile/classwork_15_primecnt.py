import math
import time

def checkprime(x):
    if x <= 1:
        return False
    for i in range(2,int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True


#----main----
n = eval(input('n='))
time1 = time.time()
cnt = 0
for i in range(2,n+1):
    if checkprime(i):
        cnt += 1
time2 = time.time()
print(time2-time1)
print('\ncnt: '+str(cnt))
