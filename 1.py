import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = []
while True:
    s = input("Ціле додатнє число: ")
    if s == "":
        break
    elif int(s) <= 0:
        print("Ціле додатнє!")
        break
    else:
        l.append(int(s))
if len(l) < 6:
    print("Помилочка")
else:
    for  i in range(3):
        l.remove(max(l))
        l.remove(min(l))
print(l)
printTimeStamp("Доброштан і Глигало")
