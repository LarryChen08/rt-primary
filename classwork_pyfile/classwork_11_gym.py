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

def roundnum(a, b = 1):
    a = int(a * (10**b) + 0.5)
    a /= 10**b
    return a


scList = [9.8, 9.2, 9.5, 10, 9.4, 10, 9.3, 9.7]
stList = sortlist(scList)
sum1 = sum(scList)
sum2 = sum(stList[1:-1])
print('sum1: '+str(roundnum(sum1/len(scList),3)))
print('sum2: '+str(roundnum(sum2/(len(stList)-2),3)))
print('index: '+str(scList.index(stList[-1])+1))



