wage = eval(input('please input your wage:'))
a = wage
sum = 0

taxList = [5000,3000,9000,13000,10000,20000,25000]
tax = [0,0.03,0.1,0.2,0.25,0.3,0.35,0.45]
for i in range(8):
    if i == 7:
        sum += a*tax[i]
        break
    if a <= taxList[i]:
        sum += a*tax[i]
        break
    sum += taxList[i]*tax[i]
    a -= taxList[i]
print('your final wage: ' + str(wage-sum))



wage = eval(input('input your final wage:'))
sum = 0

taxList = [5000,3000,9000,13000,10000,20000,25000]
taxList2 = [5000,2910,8100,10400,7500,14000,16250]
tax = [0,0.03,0.1,0.2,0.25,0.3,0.35,0.45]

for i in range(8):
    if i == 7:
        sum += wage/(1-tax[i])     
        break
    if wage <= taxList2[i]:
        sum += wage/(1-tax[i])
        break
    sum += taxList[i]
    wage -= taxList2[i]
print('your initial wage: ' + str(sum))



