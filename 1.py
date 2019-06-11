import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
def gcd(x,y):
    if (x == y):
        return y
    if (x < y):
        return gcd(x, y-x)
    if (x > y):
        return gcd(x-y, y)
print(gcd(x=int(input("x: ")), y=int(input("y: "))))
printTimeStamp("Доброштан і Глигало")
