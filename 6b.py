import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Place = input("Місце проживання: ")
if Place == "Будинок":
    Time = int(input("Час вдома: "))
    if Time >= 18:
        print("В'єтнамське порося")
    elif Time < 10:
        print("Змія")
    else:
        print("Собака")
elif Place == "Квартира" :
    Time = int(input("Час вдома: "))
    if Time > 10:
        print("Кішка")
    else:
        print("Хом'як")
elif Place == "Гуртожиток":
    Time = int(input("Час вдома: "))
    if Time > 6:
        print("Рибки")
    else:
        print("Мурашник")
printTimeStamp("Денис")
