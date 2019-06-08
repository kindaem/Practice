import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = int(input("Перше число: "))
m = int(input("Друге число: "))
while n != 0 and m != 0:
    if n > m:
        n %= m
    else:
        m %= n
print(n+m)
printTimeStamp("Денис")
