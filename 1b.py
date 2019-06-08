import datetime
import math
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
p = int(input("Тиск: "))
v = int(input("Об'єм: '"))
t = int(input("Температура: "))
t = t+273.15
print((p*v)/(8.314*t), "молей")
print((20000000*12)/(8.314*20), "молей в SCUBA tank який містить 12 літрів газу під тиском 20,000,000 Па. Беремо кімнатну температуру (20º)")
printTimeStamp("Денис")
