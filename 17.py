import math
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
s = int(input("Плоша: "))
n = int(input("Кількість сторін: "))
print((n*s**2)/(4*math.tan(math.pi/n)))
printTimeStamp("Денис")
