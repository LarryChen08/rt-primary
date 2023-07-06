n = int(input('n='))

for y in range(n):
    outstr = ''
    for x in range(n-y-1):
        outstr += '  '
    for z in range(y*2+1):
        outstr += '* '
    print(outstr)

for y in range(n-2,-1,-1):
    outstr = ''
    for x in range(n-y-1):
        outstr += '  '
    for z in range(y*2+1):
        outstr += '* '
    print(outstr)

'''
for i in range(n-1):
    outstr = ''
    for j in range(i+1):
        outstr += ' '
    for k in range(2*(n-i)-3):
        outstr += '*'
    print(outstr)
'''