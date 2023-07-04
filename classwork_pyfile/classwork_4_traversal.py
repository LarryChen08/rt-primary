h, f = eval(input('input the number of heads and feets:'))
'''
if h*2 > f or h*4 < f or f%2 == 1:
    print('no answer')
    '''

for i in range(h+1):
    if i*4 + (h-i)*2 == f:
        print('rabbit: '+str(i),'rooster: '+str(h-i))
        break
    if i == h:
        print('no answer')



print('\\')


