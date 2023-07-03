tBeginPrice = 16
tBeginDst = 3
tPrice = 2.5
tLongDst = 15
dPrice = 2.4
dMin = 13
uPrice = 2.17
uMin = 15
#d = eval(input('distance:'))

for d in range(50,201,1):
    d /= 10
    #Taxi
    
    if d < tBeginDst:
        d1, d2 = 0, 0
    elif d < tLongDst:
        d1, d2 = d - tBeginDst, 0
    else:
        d1, d2 = tLongDst - tBeginDst, d - tLongDst
    tMoney = tBeginPrice + d1*tPrice + d2*tPrice*1.5

    #Didi
    dMoney = dPrice*d
    if dMoney < dMin:
        dMoney = dMin
    #Uber
    uMoney = uPrice*d
    if uMoney < uMin:
        uMoney = uMin
    print('km: ' + str(d))
    print('Taxi: ' + str(tMoney))
    print('Didi: ' + str(dMoney))
    print('Uber: ' + str(uMoney))


