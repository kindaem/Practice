import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = []
q = []
while True:
    s = input("Слово: ")
    if s == "":
        break
    l.append(s)
    for i in l:
        if i not in q:
            q.append(i)
print(q)
printTimeStamp("Доброштан і Глигало")
