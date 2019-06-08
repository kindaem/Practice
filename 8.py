import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Sht = int(input("Скільки штучок: "))
Shtyk = int(input("Скільки штукенцій: "))
print("Загальна маса замовлення: ", Sht*75 + Shtyk*112, "грам")
printTimeStamp("Денис")
