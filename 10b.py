import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
t1 = int(input("t1: "))
g1 = int(input("g1: "))
t2 = int(input("t2: "))
g2 = int(input("g2: "))
l = 6371.01*math.acos(math.radians(math.sin(math.radians(t1))*math.sin(math.radians(t2)) + math.cos(math.radians(t1))*math.cos(math.radians(t2))*math.cos(math.radians(g1 - g2))))
print(l)
printTimeStamp("Денис")
