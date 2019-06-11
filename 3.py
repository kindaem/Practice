import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
def expt(b, n):
    if n==0:
        return 1
    return b*expt(b, n-1)
print(expt(b=int(input("b:")), n=int(input("n: "))))
printTimeStamp("Доброштан і Глигало")
