import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
n = input("Введите 4-значное число: ")
l = list(n)
d1 = int(l[0])
d2 = int(l[1])
d3 = int(l[2])
d4 = int(l[3])
print("Сумма цифр числа:", d1 + d2 + d3+ d4 )
printTimeStamp("Денис")
