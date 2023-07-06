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

aList = eval(input('aList[]='))
bList = sortlist(aList)

'''for a in aList:
    s += a
    if aMax < a:
        aMax = a'''

print('max: '+str(bList[0])+'\tmaxid: '+str(aList.index(bList[0])+1))
print('min: '+str(bList[-1])+'\tminid: '+str(aList.index(bList[-1])+1))
print('max2: '+str(bList[1])+'\tmax2id: '+str(aList.index(bList[1])+1))
print('min2: '+str(bList[-2])+'\tmin2id: '+str(aList.index(bList[-2])+1))