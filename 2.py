import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
def catalan(n):
    if n >= 2:
        c = ((2 * ((2*n) - 1)) / (n+1)) * catalan(n-1)
        return int(c)
    return 1
print(catalan(n = int(input("n: "))))
printTimeStamp("Доброштан і Глигало")
