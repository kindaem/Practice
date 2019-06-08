import datetime
from math import pi
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
r = int(input("Радіус: "))
print("Об'єм:", (4/3)*pi*r**3, "Площа: ", 4*pi*r**2)
printTimeStamp("Денис")
