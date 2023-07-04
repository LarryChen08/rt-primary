#Casino1
import random
dMax = 0
for i in range(3):
    print('Round '+str(i+1))
    input('Go!')
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    if d1 + d2 > dMax:
        dMax = d1 + d2
    print('Dice1: '+ str(d1) + '\tDice2: '+str(d2)+'\tScore: '+str(d1+d2))
print('Best: '+str(dMax))


#Casino2
import random

dMax = 0
PointList = [[],[],[]]
ScoreList = [0,0]
winDic = {'Pwin':0,'Cwin':0,'Draw':0}
for i in range(3):
    print('Round '+str(i+1))
    input('Go!')
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    score1 = d1+d2
    ScoreList[0]+=score1
    print('Player\tDice1: '+ str(d1) + '\tDice2: '+str(d2)+'\tScore: '+str(score1))
    d3 = random.randint(1, 6)
    d4 = random.randint(1, 6)
    score2 = d3+d4
    ScoreList[1]+=score2
    print('CPU\tDice1: '+ str(d1) + '\tDice2: '+str(d2)+'\tScore: '+str(score2))
    if score1 > score2:
        print('You win!')
        winDic['Pwin']+=1
    elif score1 < score2:
        print('CPU win!')
        winDic['Cwin']+=1
    else:
        print('Draw!')
        winDic['Draw']+=1
print('Player win:',winDic['Pwin'],'\tCPU win:',winDic['Cwin'],'\tDraw:',winDic['Draw'])
if winDic['Pwin'] == winDic['Cwin']:
    if ScoreList[0] > ScoreList[1]:
        print('Player win!')
    elif ScoreList[0] < ScoreList[1]:
        print('CPU win!')
    else:
        print('Draw!')
elif winDic['Pwin'] > winDic['Cwin']:
    print('Player win!')
else:
    print('CPU win!')


#Casino3
import random
import pandas as pd
def sortlist(list1):
    resList = []
    for item in list1:
        if resList == []:
            resList.append(item)
            continue
        for i in range(len(resList)):
            if item > resList[i]:
                resList.insert(i,item)
                break
    return resList
        

df = pd.DataFrame([],columns=['dice1','dice2','dice3'])
resDic = {'baozi':0,'shunzi':0,'duizi':0,'else':0}
for i in range(100000):
    d1,d2,d3 = random.randint(1,6),random.randint(1,6),random.randint(1,6)
    dList = [d1,d2,d3]
    dList.sort(reverse=True)
    df.loc[i] = dList
    #baozi
    if d1 == d2 == d3:
        resDic['baozi'] += 1
    #shunzi
    elif d1 - d2 == 1 and d2 - d3 == 0:
        resDic['shunzi'] += 1
    #duizi
    elif d1 == d2 or d1 == d3 or d2 == d3:
        resDic['duizi'] += 1
    else:
        resDic['else'] += 1
print(resDic)
print(df)


