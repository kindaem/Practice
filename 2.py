import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = []
while True:
    s = input("Число: ")
    if s == "":
        break
    s = int(s)
    l.append(s)
cr = sum(l) / len(l)
l1 = []
l2 = []
for i in l:
    if i < cr:
        l1.append(i)
    else:
        l2.append(i)
print(l1)
print(l2)
print(cr)
printTimeStamp("Доброштан і Глигало")
