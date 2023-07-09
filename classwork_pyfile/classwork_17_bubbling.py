nList = list(eval(input('[]:')))
indexList = list(range(1, len(nList)+1))

for a in range(len(nList)-1):
    flag = 0
    for i in range(len(nList)-1-a):
        if nList[i] < nList[i+1]:
            nList[i], nList[i+1] = nList[i+1], nList[i]
            indexList[i], indexList[i+1] = indexList[i+1], indexList[i]
            flag = 1
    print(nList)
    print(indexList)
    if flag == 0:
        break
print('---------')
print(nList)
print(indexList)