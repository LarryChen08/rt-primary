def prime(x):
    res = []
    for i in range(2,int(x**0.5//1+1)):
        if x % i == 0:
            while True:
                if x % i == 0:
                    res.append(i)
                    x /= i
                else:
                    break
            if x == 1:
                return res
            continue

        


a, b = eval(input('a,b='))
if b > a:
    a, b = b, a
bList = prime(b)
GCD = 1
for i in bList:
    if a % i == 0:
        a /= i
        GCD *= i
print('LCM: '+str(int(a*b)))
print('GCD: '+str(GCD))

a, b = eval(input('a,b='))
if b > a:
    a, b = b, a
for n in range(a,a*b+1,a):
    if n % a == 0 and n % b == 0:
        print('LCM: '+str(n))
        break

for i in range(b,0,-1):
    if a % i == 0 and b % i == 0:
        print('GCD: '+str(i))
        break


print(2**0.5//1)


