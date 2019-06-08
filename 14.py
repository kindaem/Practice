import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Bread_1 = int(input("Кільскість вчорашнього хлібу: "))
Bread_2 = int(input("Кільскість сьогоднішнього хлібу: "))
print("Cума грошей за звичайну кількість товару {0:>30}" .format((Bread_1 + Bread_2)*8.50 ))
print("Скидка: {0:>63}"  .format((Bread_1)*8.50*0.6))
print("Всього: {0:>63}"  .format((Bread_1)*8.50*0.6 + Bread_2*8.50))
printTimeStamp("Денис")
