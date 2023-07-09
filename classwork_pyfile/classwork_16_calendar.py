def leapyear(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

def leapyear2(n):
    out = 0
    if n % 4 == 0:
        out = 1
    if n % 100 == 0:
        out = 0
    if n % 400 == 0:
        out = 1
    return out
     


monthList = [31,28,31,30,31,30,31,31,30,31,30,31]

year, month = eval(input('input year and month:'))

if month != 2:
    print(monthList[month-1])
else:
    print(monthList[month-1]+leapyear(year))

         
         
    
