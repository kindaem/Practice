import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
Year = int(input("Year: "))
if Year % 400 == 0:
    print("Рік високосний")
else:
    if Year % 100 == 0 and Year % 4 == 0:
        print("Рік високосний")
    else:
        print("Рік не високосний")
printTimeStamp("Денис")
