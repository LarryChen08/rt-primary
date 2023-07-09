import math
r = int(input('Input the radius:'))
for y in range(r,-1,-1):
    x = int(math.sqrt(r*r-y*y))
    outstr = ''
    for i in range(r-x):
        outstr += '  '
    for j in range(x*2+1):
        outstr += '* '
    print(outstr)

for y in range(1,r+1):
    x = int((r*r-y*y)**0.5)
    outstr = ''
    for i in range(r-x):
        outstr += '  '
    for j in range(x*2+1):
        outstr += '* '
    print(outstr)
    
