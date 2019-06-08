import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
l = int(input("Ваш ріст: "))
print("Ріст в дюймах: ", l/2.54, "а ріст в футах: ", l/2.54/12)
printTimeStamp("Денис")
