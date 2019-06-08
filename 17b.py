import datetime
from math import sqrt
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
m = int(input("Маса води: "))
dt = int(input("Температурна зміна: "))
q = 4.186
C = q/(m*dt)
print(C)
print("Для 250 мл кави потрібно: ", (q/(250*80))*2.7*10**(-7)*1.33,"грн")
printTimeStamp("Денис")
