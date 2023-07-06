nmin, nmax = eval(input('range:'))
sum,num = 0, 0

#list method
'''
resList = [1,1]
for i in range(n):
    resList.append(resList[i]+resList[i+1])
print(resList)
'''

#variable method
n1, n2 = 1,1
while True:
    n1, n2 = n2, n1+n2
    if n2 >= nmin:
        print(n2)
        if n2 <= nmax:
            sum += n2
            num += 1
            continue
        print('num: '+str(num)+'\nsum: '+str(sum))
        break
