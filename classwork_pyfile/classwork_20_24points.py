
places = '0123'
def recursion(ans):
    global resList
    if len(ans)== 4: 
        resList.append(ans)
    for c in places:
        if c in ans:
            continue
        ans += c
        recursion(ans)
        ans = ans[:-1]
    return resList


answers = []
resList = []
print(recursion(''))

'''
def rearrange():
    resList = []
    for p1 in range(4):
        for p2 in range(4):
            if p1 == p2:
                continue
            for p3 in range(4):
                if p1 == p3 or p2 == p3:
                    continue
                resList.append([p1,p2,p3,6-p1-p2-p3])
    return resList'''


while True:
    try:
        pList = eval(input('input 4 poker cards:'))
    except:
        print('The input is wrong. Please re-input')  
        continue  
    if len(pList) != 4:
        print('The input is wrong. Please re-input')  
        continue  
    flag = 0
    for p in pList:
        if p < 1 or p > 13 or p != int(p):
            flag = 1
    if flag == 1:
        print('The input is wrong. Please re-input')
    break
    


cList = ['+', '-', '*', '/']
result_List = recursion('')

kList = [['','','','','',''],
         ['(','',')','','',''],
         ['','(','','',')',''],
         ['','','','(','',')'],
         ['(','','','',')',''],
         ['','(','','','',')'],
         ['(','',')','(','',')']]

for item in result_List:
    p1, p2, p3, p4 = int(item[0]), int(item[1]), int(item[2]), int(item[3])
    for c1 in range(4):
        for c2 in range(4):
            for c3 in range(4):
                for k in kList:
                    s = k[0] + str(pList[p1]) + cList[c1] + k[1]+ str(pList[p2]) + \
                        k[2] + cList[c2] + k[3] + str(pList[p3]) + k[4] + cList[c3] \
                        + str(pList[p4]) + k[5]
                    try:
                        if 23.99 < eval(s) < 24.01:
                            print(s)
                    except:
                        pass

