import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))

now = datetime.datetime.now()
print(now + datetime.timedelta(seconds=int(input("Кількість секунд: "))))
printTimeStamp("Денис")
