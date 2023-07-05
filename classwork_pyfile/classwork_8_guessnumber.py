bottom, top = 1,101
xList = []

while bottom != top:
    x = int((bottom + top)/2)
    '''
    if x in xList:
        print('Your input is wrong')
        break'''
    if x == top or x == bottom:
        print('Your input is wrong')
        break
    xList.append(x)
    print(x,bottom,top)
    if bottom + 2 == top:
        print('The answer is: '+str(x))
        break
    print('I guess '+str(x))
    ans = input('> or < or =: ')
    if ans == '>':
        top = x
        continue
    if ans == '<':
        bottom = x
        continue
    print('The answer is: '+str(x))
    break


