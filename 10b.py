import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
ip = input("IPv4: ")
if len(ip) <= 6 or len(ip) >= 16:
    print("Помилочка")
else:
    l = list(ip.split("."))
    for i in l:
        if int(i) < 0 or int(i) > 255:
            print("Невірна адреса IPv4")
        else:
            pass
    print("All good")
printTimeStamp("Доброштан і Глигало")
