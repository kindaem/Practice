import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input("Число: "))
print(n*(n+1)/2)
printTimeStamp("Денис")
