# 结业测评
# 1. A
# 2. D
# 3. D
# 4. A
# 5. C
# 6. B
# 7. B
# 8. B
# 9. B
# 10. B

# 1. %
# 2. -
# 3. 10
# 4. 6
# 5. 3
# 6. 5 - y
# 7. a > 0
# 8. a <= 1
# 9. i
# 10. -2

# 编程部分
# 1. 质数统计
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

#----main----
n, width = eval(input('please input n and width: '))
k, n = n // width, n % width
df = pd.DataFrame([],columns = ['range', 'number'])
for i in range(k):
    cnt = 0
    for j in range(1 + width * i,width * (i + 1) + 1):
        if checkprime(j):
            cnt += 1
    ran = '(' + str(1 + width * i) + '-' + str(width * (i + 1)) + ')'
    df.loc[i] = [ran, cnt]


cnt = 0

if n != 0:
    for p in range(k * width + 1, k * width + 1 + n):
        if checkprime(p):
            cnt += 1
    ran = '(' + str(k * width + 1) + '-' + str(k * width + n) + ')'
    df.loc[i+1] = [ran, cnt]


for q in range(len(df)):
    outstr = '*' * df.iloc[q,1] + df.iloc[q,0]
    print(outstr)


# 2. nested loop
h = int(input('h='))
# a)
resStr = ''
for x in range(h):    
    for y in range(x):
        resStr += ' '
    for y in range(2 * (h - x) - 1):
        resStr += '*'
    resStr += '\n'
print(resStr)

# b)
resStr = ''
for x in range(h):    
    for y in range(h - x - 1):
        resStr += ' '
    for y in range(x + 1):
        resStr += str(y + 1)
    resStr += '\n'
print(resStr)

# c)
resStr = ''
for x in range(h):    
    for y in range(h - x - 1):
        resStr += ' '
    for y in range(x + 1):
        resStr += str(y + 1)
    for y in range(x, 0, -1):
        resStr += str(y)
    resStr += '\n'
print(resStr)
    
# d)
resList = []
for x in range(h * 2):  
    resStr = ''  
    for y in range(h * 2 - 1 - x):
        resStr += ' '
    for y in range(x * 2 + 1):
        resStr += '*'
    resList.append(resStr)

for x in range(h):
    resStr = resList[h + x]
    resStr = resStr[:h + x] + ' ' * (2 * (h - x) - 1) + resStr[- x * 2 - 1:]
    resList[h + x] = resStr
print('\n'.join(resList))


# 3. 诈金花 monte carlo
import random

def sortlist(list1):
    resList = []
    for item in list1:
        if resList == []:
            resList.append(item)
            continue
        for i in range(len(resList)):
            if item >= resList[i]:
                resList.insert(i,item)
                break
            if i+1 == len(resList):
                resList.append(item)
    return resList

def check(a):
    out_list = [0,0,0,0,0]
    for i in range(a):
        d1,d2,d3 = random.randint(1,6),random.randint(1,6),random.randint(1,6)
        dList = [d1,d2,d3]
        dList = sortlist(dList)       
        #baozi
        if d1 == d2 == d3:
            out_list[0] += 1
        #shunzi
        elif dList[0] - dList[1] == 1 and dList[1] - dList[2] == 1:
            out_list[1] += 1
        #duizi
        elif d1 == d2 or d1 == d3 or d2 == d3:
            out_list[2] += 1
        #sanbukao
        elif dList[0] - dList[1] > 1 and dList[1] - dList[2] > 1:
            out_list[3] += 1
            print(d1,d2,d3)
        #else
        else:
            out_list[4] += 1
    return out_list

n = int(input('n='))
print(check(n))


# 4. List data analyze
nList = eval(input('nList='))
s = 0
half = (len(nList) - 1) / 2
half1s, half2s = 0, 0
for i in range(len(nList)):
    s += nList[i]
    if i <= half:
        half1s += nList[i]
    if i >= half:
        half2s += nList[i]
print('sum=' + str(s))
print('avg=' + str(s/len(nList)))
print('half1 avg=' + str(half1s/int(half+1)))
print('half2 avg=' + str(half2s/int(half+1)))

# 5. 四则运练习
import random

kList = ['-', '+', '*', '/']
cnt = 0
for i in range(10):
    while True:
        a, b = random.randint(0, 100), random.randint(0, 100)
        k = random.randint(0,31)      
        if k == 0:
            ans = a - b
        elif k == 1:
            ans = a + b
        elif 2 <= k and 12:
            k = 2
            ans = a * b
        else:
            if b == 0:
                continue
            k = 3
            ans = a / b
        exp = str(a) + ' ' + kList[k] + ' ' + str(b) + ' ='
        if ans >= 0 and ans <= 100 and int(ans) == ans:
            ans_user = eval(input(exp))
            if ans_user == ans:
                print('correct!')
                cnt +=  10
                break
            print('wrong!')
            break
print('score: ' + str(cnt))





