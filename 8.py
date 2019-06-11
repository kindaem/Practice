import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
from pprint import pprint
carts = []
mast = ['s', 'h', 'd', 'c']
num = ['J', 'Q', 'K', 'A']
for i in range(len(mast)):
    for a in range(2, 11):
        b = str(a) + str(mast[i])
        carts.append(b)
    for z in range(len(num)):
        b = str(num[z]) + str(mast[i])
        carts.append(b)
print(carts)
from random import randrange
def sattoloCycle(items):
    h = len(items)
    while h > 1:
        h = h - 1
        j = randrange(h)  # 0 <= j <= i-1
        items[j], items[h] = items[h], items[j]
    return
print(sattoloCycle(carts))
