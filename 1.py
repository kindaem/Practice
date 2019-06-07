
import datetime
def printTimeStamp(name):
    print('Автор програми: ' + name)
    print('Час компіляції: ' + str(datetime.datetime.now()))
m = int(input("Маса: "))
l = int(input("Ріст: "))
imt = m/(l*l)
print("Індекс маси тіла: ", imt)
printTimeStamp("Денис")
