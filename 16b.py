import datetime
from math import sqrt
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
x = int(input("Enter the x part of the coordinate: "))
y = int(intpu("Enter the y part of the coordinate: "))
xy = []
while True:
    x1 = int(input("Enter the x part of the coordinate: (blank to quit): "))
    y1 = int(input("Enter the y part of the coordinate: ")
    xy.append(x1, y1)
    if x1 == " ":
        break
xy.pop()
