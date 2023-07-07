import math
import pandas as pd
import matplotlib.pyplot as plt

#----main----
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

n = int(input('please input the range: '))
k, n = n // 100, n % 100
df = pd.DataFrame([],columns = ['range', 'number'])
ran1, ran2 = 1, 101
for i in range(k):
    cnt = 0
    for j in range(ran1,ran2):
        if checkprime(j):
            cnt += 1
    ran = '(' + str(ran1) + '-' + str(ran2-1) + ')'
    df.loc[i] = [ran, cnt]
    ran1 += 100 
    ran2 += 100

cnt = 0

if n != 0:
    for p in range(ran2-100, ran2 + n - 100):
        if checkprime(p):
            cnt += 1
    ran = '(' + str(ran2-100) + '-' + str(ran2 + n - 101) + ')'
    df.loc[i+1] = [ran, cnt]

'''
for q in range(len(df)):
    outstr = '*' * df.iloc[q,1] + df.iloc[q,0]
    print(df.iloc[q,1])
    print(outstr)'''

x = df['range']
y = df['number']

plt.bar(x,y,width=0.8,label='number of primes')
plt.title('Appereance comparison of primes')
plt.ylabel('Times')
plt.xlabel('Range')
plt.ylim(0,40)
for a,b in zip(x,y):
    plt.text(a,b,b,va='bottom',ha='center')
plt.grid(axis='y')
plt.legend(loc='upper left')

plt.show