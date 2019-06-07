import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
P = int(input("Тиск, (кПа): "))
ftdm = P/6.89
atm = P/101.325
mm = P/7.501
print("кПа = ", ftdm, "фт/дм^2Б", mm, "мілісетрів ртутного стовпчика,", atm,"атмосфер.")
printTimeStamp("Денис")
