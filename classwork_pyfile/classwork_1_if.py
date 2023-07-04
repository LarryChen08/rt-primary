import time,pandas
pApple = 3.5
a, b = eval(input('weight of apples and bananas:'))
sum = 0

# if
# <5
if b <= 5:
    sum += b*5.5
    b = 0
else:
    sum += 5*5.5
    b -= 5
# 5-10
if b <= 5:
    sum += b*5.5*0.8
    b = 0
else:
    sum += 5*5.5*0.8
    b -= 5
# 10-20
if b <= 10:
    sum += b*5.5*0.7
    b = 0
else:
    sum += 10*5.5*0.7
    b -= 10
# >20
sum += b*5.5*0.6
print('price: '+str(sum+a*pApple))

#loop-extra
aList = [5,5,10]
price = [1,0.8,0.7,0.6]
for i in range(4):
    if i == 3:
        sum += b*5.5*price[i]
        print('price: '+str(sum+a*pApple))
        break
    if b <= aList[i]:
        sum += b*5.5*price[i]
        print('price: '+str(sum+a*pApple))
        break
    sum += aList[i]*5.5*price[i]
    b -= aList[i]


