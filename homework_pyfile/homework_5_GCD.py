a, b = eval(input('Please input two numbers:'))
if b > a:
    a, b = b, a

c = a % b


while True:
    if c == 0:
        print('GCD: '+str(b))
        break
    a, b = b, c
    c = a % b
    
