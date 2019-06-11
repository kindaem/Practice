import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = int(input('Введіть число:'))
b = 0
l = []
for i in range(2, a+1):
    l.append(i)
for z in l:
    s = l[b]
    b += 1
    if z**2 >= a:
        break
    for i in l:
        if i % s == 0 and i != s:
            l.remove(i)
print(l)
printTimeStamp("Доброштан і Глигало")
