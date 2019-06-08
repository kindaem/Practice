import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
a = input("ISBN: ")
l = list(a)
sum = int(l[0]) + int(l[1])*3 + int(l[2]) + int(l[3])*3 + int(l[4]) + int(l[5])*3 + int(l[6]) + int(l[7])*3 + int(l[8]) + int(l[9])*3 + int(l[10]) + int(l[11])*3
num = 10 -(sum%10)
print("Перевірочна цифра:", num)
printTimeStamp("Денис")
