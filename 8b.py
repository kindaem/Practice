import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = []
while True:
    s = (input("Символ адреси: "))
    l.append(s)
    if s == "":
        break
l.pop()
if len(l) < 6 or len(l) > 7:
    print("Wrong address")
else:
    if (l[1]) and (l[2]) and (l[3]) and (l[4]) is int:
        print("New type of address")
    else:
        print("old type")
printTimeStamp("Денис")
