n = eval(input('n='))
s = 0
aMax = 0
nMax = 0
aMax2 = 0
nMax2 = 0

aMin = 100
nMin = 0
aMin2 = 100
nMin2 = 0

for i in range(n):
    print('No. '+str(i+1))
    a = eval(input('a='))
    if a > aMax2:
        aMax2,nMax2 = a, i
        if aMax2 > aMax:
            aMax2,aMax = aMax, aMax2
            nMax2,nMax = nMax, nMax2          
    if a < aMin2:
        aMin2,nMin2 = a, i
        if aMin2 < aMin:
            aMin2,aMin = aMin, aMin2
            nMin2,nMin = nMin, nMin2  
    s += a

print('sum: '+str(s))
print('Min: '+str(aMin)+' No. '+str(nMin+1))
print('Min2: '+str(aMin2)+' No. '+str(nMin2+1))
print('Max: '+str(aMax)+' No. '+str(nMax+1))
print('Max2: '+str(aMax2)+' No. '+str(nMax2+1))


