import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
from pprint import pprint
s = []
h = []
d = []
c = []
mast = ['s', 'h', 'd', 'c']
num = ['J', 'Q', 'K', 'A']
for i in range(len(mast)):
    for a in range(2, 11):
        b = str(a) + str(mast[i])
        if i == 1:
            s.append(b)
        elif i == 2:
            h.append(b)
        elif i == 3:
            d.append(b)
        else:
            c.append(b)
    for z in range(len(num)):
        b = str(num[z]) + str(mast[i])
        if i == 1:
            s.append(b)
        elif i == 2:
            h.append(b)
        elif i == 3:
            d.append(b)
        else:
            c.append(b)
print("{0}\n{1}\n{2}\n{3}".format(s,h,d,c))
printTimeStamp("Доброштан і Глигало")
